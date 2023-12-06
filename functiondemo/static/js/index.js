<<<<<<< HEAD:server/static/js/index.js
=======

const app = new Vue({
  delimiters: ["{:", ":}"],
  data() {
    return {
      proc:'',
      result:''
    }
  },
  methods: {
    loadDatas: function(){
      let self = this;
      axios.get("/api/data/search/" + self.proc).then(resp=>{
        console.log("load datas", resp);
        let data = resp.data;
        if(data.code == 0){
          self.result = JSON.stringify(data.data);
        }
      });
    },
  },
  computed: {
  },
  created() {
  },
  mounted: function(){
  }

}).$mount('#container');
>>>>>>> ae3b4160909a27ffe7fd44aebd9f3a46d11d1e9b:functiondemo/static/js/index.js
