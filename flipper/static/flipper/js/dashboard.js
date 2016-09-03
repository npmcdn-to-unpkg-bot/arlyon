var Container = React.createClass({
    loadItemsFromServer: function() {
        $.ajax({
            url: this.props.url,
            dataType: 'json',
            cache: false,
            success: function(data) {
            this.setState({data: data});
            }.bind(this),
            error: function(xhr, status, err) {
            console.error(this.props.url, status, err.toString());
            }.bind(this)
        });
    },
    getInitialState: function() {
        return {data: []};
    },
    componentDidMount: function() {
        this.loadItemsFromServer();
        setInterval(this.loadItemsFromServer, this.props.pollInterval);
    },
    render: function() {
        console.log('container')
        return (
        <div className="row">
            <Zone name="BuyingBox" flipstatus="1" flips={this.state.data} />
            <Zone name="BankBox" flipstatus="2" flips={this.state.data} />
            <Zone name="SellingBox" flipstatus="3" flips={this.state.data} />
        </div>
    );
  }
});

var Zone = React.createClass({
    render: function() {
        var data = this.props.flips
        var flipstatus = this.props.flipstatus
        var statusdata = []
        for (var i = 0; i < data.length; i++) {
            if (data[i]["fields"]["flipstatus"] == flipstatus) {
                statusdata.push(data[i])
            };
        };
        return (
            <div className="col s12 l4">
                <h1 className="center">{this.props.name}</h1>
                <Entry data={statusdata}></Entry>
            </div>
        );
    }
});

var Entry = React.createClass({

    onButtonClick: function (event, flipstatus, flipid) {
        console.log(flipstatus)
        if (flipstatus == 1) {
            console.log("success")
            var message = 'Send item to the bank?'
            var inputtext = []
        }
        else if (flipstatus == 2) {
            var message = 'Put item on the market?'
            var inputtext = [
                '<div class="vex-custom-field-wrapper">',
                    '<label for="sellprice">Price</label>',
                    '<div class="vex-custom-input-wrapper">',
                        '<input name="sellprice" type="number" value="0" />',
                    '</div>',
                '</div>',
            ]
        }
        else if (flipstatus == 3) {
            var message = 'Register successful sale?'
            var inputtext = []
        }
        console.log(message)
        vex.dialog.open({
            message: message,
            input: inputtext.join(''),
            callback: function (data) {
                console.log(data, flipid)
                if (!data) {
                    return console.log('Cancelled')
                }
                if (data.sellprice == 0) {
                    Materialize.toast(`You can't sell items for 0gp.`, 4000)
                }
                else {
                   $.ajax({
                       url: "flipupdate",
                       type:"GET",
                       data: {flip:flipid, sellprice:data.sellprice, flipstatus:flipstatus}
                   });
                   Materialize.toast(`Selling.`, 4000)
                }
            }
        })
    },

    render: function() {
        var itemList = this.props.data.map(function(items) {
            if (items.fields.flipstatus == 1) {
                var timeago = jQuery.timeago(items.fields.requestdate)
                var price = gpify(items.fields.buyprice)
                var advancename = "bank"
            }
            else if (items.fields.flipstatus == 2) {
                var timeago = jQuery.timeago(items.fields.purchasedate)
                var price = gpify(items.fields.buyprice)
                var advancename = "market"
            }
            else {
                var timeago = jQuery.timeago(items.fields.listeddate)
                var price = gpify(items.fields.sellprice)
                var advancename = "sold"
            }
            return (
                <div className="card horizontal" key={items.pk}>
                    <div className="card-image valign-wrapper">
                        <img id="card-icon" className="valign hide-on-small-only" src={"/static/flipper/images/big/"+items.fields.item_id+".gif"}></img>
                    </div>
                    <div className="card-stacked">
                        <div className="card-content" id="itemcard">
                            <div className="row nopadding valign-wrapper">
                                <div className="col s7">
                                    <h4 className="nopadding"><b>{items.fields.item_name}</b></h4>
                                    <div>{timeago}</div>
                                </div>
                                <div className="col s4">
                                    <div>
                                        <div><b>Price: </b>{price}</div>
                                    </div>
                                </div>
                                <div className="col s1">
                                    <i className="material-icons right activator">more_vert</i>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div className="card-reveal nopadding">
                        <div className="card-stacked">
                            <div className="card-content" id="itemcard">
                                <div className="row nopadding valign-wrapper">
                                    <div className="col s7">
                                        <h4 className="nopadding"><b>{items.fields.item_name}</b></h4>
                                        <div>{timeago}</div>
                                    </div>
                                    <div className="col s4">
                                        <button onClick={() => this.onButtonClick(event, items.fields.flipstatus, items.pk)} className="btn right" id={"to"+advancename}>
                                            {advancename}
                                        </button>
                                    </div>
                                    <div className="col s1">
                                        <span className="card-title"><i className="material-icons right activator">close</i></span>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            );
        }, this);
        return (
            <div className="itemsList">
                {itemList}
            </div>
        );
    }
});

ReactDOM.render(
  <Container name="Container" url="json" pollInterval={2000}/>,
  document.getElementById("app")
);
