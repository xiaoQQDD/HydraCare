
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