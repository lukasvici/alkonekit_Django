function add(id){
  $.post("../cartadd/", {"id":id, "amount":1},
  function(data){
    if(data != ""){
      $(".cart b").text((parseInt($(".cart b").text()) + data["price"])+"₽");
    }
  });
}
function amountplus(id){
  $.post("../amount/", {"id":id,"type":"plus"},
  function(data){
    localprice(data);
    amountchange(data);
    changepricecart(data);
  });
}
function amountminus(id){
  $.post("../amount/", {"id":id, "type":"minus"},
  function(data){
    localprice(data);
    amountchange(data);
    changepricecart(data);
  });
}

function changepricecart(data){
  console.log("dfafaw")
  $(".block-top p:last-child").text(data["allprice"]+"₽")
  $("#cart b").text(data["allprice"]+"₽")
}


function localprice(data){
  $("#price"+data["id"]).text((data["price"]*data["amount"])+"₽")
}
function amountchange(data){
  if (data["amount"] == 0){
    $("#prod"+data["id"]).remove();
  }
  else
    $("#amount"+data["id"]).text(data["amount"]);
}


function sendtelegram(){
  $.post("../sendtelegram/", {});
}

