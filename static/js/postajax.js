function add(id){
  $.post("../cartadd/", {"id":id, "amount":1},
  function(data){
    console.log(data["price"]);
    $(".cart b").text(data["price"],"₽");
  });
}
function amountplus(id){
  $.post("../amount/", {"id":id,"type":"plus"},
  function(data){
    amountchange(data);
  });
}
function amountminus(id){
  $.post("../amount/", {"id":id, "type":"minus"},
  function(data){
    amountchange(data);
  });
}


function amountchange(data){
  console.log("amount"+data["id"]);
  if (data["amount"] == 0){
    $("#prod"+data["id"]).remove();
  }
  else
    $("#amount"+data["id"]).text(data["amount"]);
}

