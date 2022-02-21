const hr = {
    data() {
      return {
        products: ["Пиво жадетское", "Водка Мароша", "Водка океан","пять озер"],
        category: ["Вина","Пиво","Шампанское","Алкоголь", "Vape","Промтовары"]
      }
    },
    methods:{
        test(){
            console.log("sdfa")
        }
    }
  }
Vue.createApp(hr).mount('#hr')
const menu = {
  data() {
    return {
      subcategory: ['<a href="#">1</a><a href="#">2</a><a href="#">1</a>'],
      category: ["Вина","Пиво","Шампанское","Алкоголь", "Vape","Промтовары"]
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