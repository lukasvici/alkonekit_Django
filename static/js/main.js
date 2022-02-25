const menu = {
  methods: {
    openSub(id) {
      $('#sub_'+id).show();
      $('#btno_'+id).hide();
      $('#btnc_'+id).show();
    },
    closeSub(id){
      $('#sub_'+id).hide();
      $('#btnc_'+id).hide();
      $('#btno_'+id).show();
    }
}
}
Vue.createApp(menu).mount('#menu')