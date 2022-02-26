const menu = {
  data() {
    return {
      category: ['<a href="../../Вина">Вина</a>','<a href="../../Пиво">Пиво</a>','<a href="../../Алкоголь">Алкоголь</a>',],
      subcategory: ['<a href="../../Вина/Красное">Красное</a><a href="../../Вина/Розовое">Розовое</a><a href="../../Вина/Белое">Белое</a>'],
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