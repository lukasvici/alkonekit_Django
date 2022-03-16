//+товар
function add(id){
  $.post("../../cartadd/", {"id":id, "amount":1},
  function(data){
    console.log(data);
    if(data != ""){
      $(".cart b").text(parseInt($(".cart b").text()) + parseInt(data["price"])+ "₽");
    }
  });
}
//+Кол-во товара
function amountplus(id){
  $.post("../amount/", {"id":id,"type":"plus"},
  function(data){
    console.log(data)
    changetextamount(data);
    amountchange(data);
  });
}
//-Кол-во товара
function amountminus(id){
  $.post("../amount/", {"id":id, "type":"minus"},
  function(data){
    changetextamount(data);
    amountchange(data);
  });
}

//изменение количества товара
function amountchange(data){
  if (data["amount"] == 0){
    $("#prod"+data["id"]).remove();
  }
  else
    $("#amount"+data["id"]).text(data["amount"]);
}
// изменение цены с учетом кол-во товара
function changetextamount(data){
  $("#price"+data["id"]+" p").text(data["price"]*data["amount"] + " ₽");
}

