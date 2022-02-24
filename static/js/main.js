const menu = {
  data() {
    return {
      category: ['<a href="#">Вино</a>','<a href="#">Пиво</a>','<a href="#">Алкоголь</a>',],
      subcategory: ['<a href="#">Красное</a><a href="#">Розовое</a><a href="#">Белое</a>'],
    }
  },
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