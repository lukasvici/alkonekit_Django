function add(id){
  console.log("fafawfw");
  $.post("../cartadd/", {"id":id, "amount":1},
  function(data, status){
    console.log(data);
  });
}