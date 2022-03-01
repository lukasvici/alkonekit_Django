function openSlideMenu () {
    document.getElementById("menu").style.right = 0;
    document.getElementById("_open").style.visibility = 'hidden';
}
function closeSlideMenu () {
    document.getElementById("menu").style.right = '';
    document.getElementById("_open").style.visibility = '';
}

function openSub(id) {
      $('#sub_'+id).show();
      $('#btno_'+id).hide();
      $('#btnc_'+id).show();
    }
function closeSub(id){
      $('#sub_'+id).hide();
      $('#btnc_'+id).hide();
      $('#btno_'+id).show();
    }