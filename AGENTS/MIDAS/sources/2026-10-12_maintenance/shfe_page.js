/** li.pengyang-v1.0.0 APP License By  */
;"use strict";

var product_options_list = [];
/*
 * @Description: content
 * @Version: 1.0
 * @Author: li.pengyang
 * @Date: 2023-08-24 11:04:46
 * @LastEditors: Please set LastEditors
 * @LastEditTime: 2023-10-23 11:23:11
 */
(function () {
  new Vue({
    el: screenWidth < 750 ? "#m_app" : "#app",
    data: {
      side_type_select: 'all', //通过url传递进来的种类参数
      searchBtn: "1",
      dayTime: [],
      value4: '',
      searchTab: 'week',
      calendarDate: new Date(),
      currentDate: "", // 当前选中日期yyyymmdd
      value2: '',
      recordYear: '',
      resultJson: {},
      //与v-model中的必须保持一致
      isCollapse: true,
      type_select: 'all',
      showDialog: false,
      // 新增参数
      form: {
        currentDate: '',
        searchBtn: '1',
        searchTab: 'week',
      },
      pro_list_info: [],
      proSelectFlag:true,
      isShowMobilePage: false,
      Contract_Series_list: ['weekQ'],
    },
    mounted: function mounted() {
      var _this = this;
      this.form.currentDate = this.calendarDate;
      this.currentDate = this.getTime(this.calendarDate);
      this.recordYear = this.currentDate.substring(0, 4);
      this.getRedJson();

      if (screenWidth < 750) {
        this.isShowMobilePage = true;
      } else {
        this.isShowMobilePage = false;
      }

      this.setDatepickerStyle();
      let pro_list = getProductList('shfe', '1');
      this.pro_list_info = pro_list.list.flat()
      // http://localhost:3007/src/table2-1/report_kx.shtml?query_options=1&query_date=20230628&query_params=delivery&query_product_code=cu
      if (window.location.href.includes('?')) {

        // 携带参数的情况下
        var test = this.analysisUrl();
        if (test.query_date) {
          var dateStr = test.query_date.replace(/^(\d{4})(\d{2})(\d{2})$/, "$1-$2-$3"); // 日期
          this.calendarDate = new Date(dateStr + ' 00:00:00');
          this.form.currentDate = this.calendarDate;

        }

        if (test.query_options) {
          if( test.query_options == '1' ) {
            pro_list = getProductList('shfe', '1');
            this.pro_list_info = pro_list.list.flat()
          } else {
            pro_list = getProductList('shfe', '2');
            this.pro_list_info = pro_list.list.flat()
          }
          this.searchBtn = test.query_options; // 期货or期权
          // this.form.searchBtn = test.query_options; // 期货or期权
        }

        if (test.query_params) {
          this.searchTab = test.query_params; // 数据筛选 -- kx
          // this.form.searchTab = test.query_params; // 数据筛选 -- kx
        }
        if (test.query_product_code) {
          var str = test.query_product_code; // 种类筛选条件 cu
          if (str === 'all' || str === 'code') {
            this.type_select = str;
            this.side_type_select = str;
          } else {
            this.type_select = getProductByGroup(str, this.searchBtn);
            this.side_type_select = this.type_select;
          }
        }


        this.$nextTick(function () {
          _this.handleTab(_this.searchTab, '', true);
        });
      } else {
        this.handleSearchTab('1')
      }
    },

    watch: {
      calendarDate: function calendarDate(newVal, oldVal) {
        this.currentDate = this.getTime(newVal);
        var str = this.currentDate.substring(0, 4);
        if (str !== this.recordYear) {
          this.recordYear = str;
          if (this.resultJson[str]) {
            this.dayTime = this.resultJson[str];
          } else {
            this.dayTime = [];
          }
        }
      }
    },
    // 新增
    computed: {
      // 小红点
      pickerOptions() {
        let that = this
        return {
          cellClassName(time) {
            let time_info = moment(time).format('YYYY-MM-DD');
            let year = moment(time).format('YYYY');
            if (that.resultJson[year] && that.resultJson[year].includes(time_info)) {
              return 'm_red_icon';
            }
          }
        }
      }
    },
    methods: {
      showDialogFn: function showDialogFn() {
        this.showDialog = true;
      },
      closeDialog: function closeDialog() {
        this.showDialog = false;
      },

      handleSearchTab: function handleSearchTab(name) {
        var vm = this;
        vm.searchBtn = name;
        if (name === '1') {
          let pro_list = getProductList('shfe', '1');
          this.pro_list_info = pro_list.list.flat();
          this.type_select = 'all';
          this.side_type_select = this.type_select;
          // this.form.searchTab = 'kx';
          this.handleTab('week');
        } else {
          let pro_list = getProductList('shfe', '2');
          this.pro_list_info = pro_list.list.flat();
          this.type_select = 'all';
          this.side_type_select = this.type_select;
          // this.form.searchTab = 'kxq';
          this.handleTab('weekQ');
        }
      },
      handleTab: function handleTab(name,channelId, isShowFirst) {
        var _this2 = this;

        var vm = this;

        if (!isShowFirst) {
          this.type_select = 'all';
          this.side_type_select = this.type_select;
        }
        // if (!isShowFirst) {
        //   if (vm.searchBtn === '1') {
        //     this.type_select = 'all';
        //   } else {
        //     this.type_select = 'all';
        //   }
        // }
        // let channelIdObj = {
        //   kx: '2471',
        //   pm: '2452',
        //   timeprice: '2475',
        //   markerprice: '2474',
        //   tradedes: '2484',
        //   js_f: '2472',
        //   dailystock: '2478',
        //   dailyDlvPlacePremium: '2480',
        //   week: '2476',
        //   weeklystock: '2479',
        //   shp: '2477',
        //   kxq: '2481',
        //   tradedes_o: '2485',
        //   jsq: '2482',
        //   weekQ: '2483',
        // }
        //console.log(this.type_select);
        // tab页添加埋点  start
            if (channelId) {
                createParams();
                params.channelId = channelId
                var strParam = "";
                for(var key in params){
                    strParam += key+"="+params[key]+"&";
                }
                strParam = strParam.substring(0,strParam.length-1);
                var trsImg =  document.createElement("img");
                trsImg.src = encodeURI(encodeURI(addUrl+"?"+strParam));
                trsImg.style.display = "none";
                document.body.appendChild(trsImg);
            }
        // tab页添加埋点  end
        vm.searchTab = name;

                
        if (vm.type_select == 'code') {
          if( !this.Contract_Series_list.includes(this.searchTab) ) {
            this.type_select = 'all';
            this.side_type_select = 'all';
          }
        }
        this.$nextTick(function () {
          _this2.$refs[name]['queryTableData_' + name]();
        });
      },

      chooseType:function( str, e ){
        this.side_type_select = e.productid;
        this.$nextTick(function () {
          this.$refs[this.searchTab]['queryTableData_' + this.searchTab]();
        });
      },

      chooseType1:function( e ){
        this.side_type_select = e;
        this.$nextTick(function () {
			if(this.searchTab=='weekQ'){
				 this.$refs[this.searchTab]['getProductionId_info'](e);
			}else{
				 this.$refs[this.searchTab]['queryTableData_' + this.searchTab]();
			}
         
        });
      },


      // 日期格式化，接收new Date日期格式
      getTime: function getTime(time) {
        var year = time.getFullYear(); //获取年份
        var month = time.getMonth() + 1; //获取月份
        var day = time.getDate(); //获取日期
        month = month < 10 ? "0" + month : month; //如果月份小于10，前面补0
        day = day < 10 ? "0" + day : day; //如果日期小于10，前面补0
        return year + "" + month + "" + day; //拼接成yyyymmdd形式字符串
      },
      timeChange: function timeChange() {
        this.calendarDate = this.value2;
        if (screenWidth < 750) {
          this.calendarDate = this.form.currentDate;
        }
      },
      handleOpen: function handleOpen(key, keyPath) {
        //console.log(key, keyPath);
      },
      handleClose: function handleClose(key, keyPath) {
        //console.log(key, keyPath);
      },
      getRedJson: function getRedJson() {
        // 日历小红点
        var vm = this;
        var jredJson = {};
        vm.resultJson = {};
        var jredUrl = api_trade_data();
        $.ajax({
          type: "GET",
          url: jredUrl,
          dataType: "text",
          success: function success(json) {

            var sp1 = json.split('return')[1];
            var sp2 = sp1.split(';});')[0];
            var sp3 = eval('(' + sp2 + ')');
            jredJson = sp3;
            var resultDate = {};
            Object.keys(jredJson).forEach(function (item) {
              var startDate = item + '-01-01';
              var endDate = item + '-12-31';
              resultDate[item] = enumerateDaysBetweenDates(startDate, endDate);
            });

            Object.keys(jredJson).forEach(function (item) {
              if (jredJson[item]) {
                vm.resultJson[item] = resultDate[item].filter(function (m) {
                  return !jredJson[item].includes(m);
                });
              } else {
                vm.resultJson[item] = resultDate[item];
              }
            });

            Object.keys(vm.resultJson).forEach(function (item) {
              vm.resultJson[item].forEach(function (m, index) {
                vm.resultJson[item][index] = m.replace(/^(\d{4})(\d{2})(\d{2})$/, "$1-$2-$3");
              });
            });
            vm.dayTime = vm.resultJson[vm.recordYear] ?  vm.resultJson[vm.recordYear] : [];
            //console.log(sp3, vm.dayTime);
          }
        });
      },

      setDatepickerStyle (){

        if (document.getElementsByClassName("el-calendar__header") && document.getElementsByClassName("el-calendar__header")[1] &&

            document.getElementsByClassName("el-calendar__header")[1].getElementsByClassName("el-calendar__button-group")[0] && 

            document.getElementsByClassName("el-calendar__header")[1].getElementsByClassName("el-calendar__button-group")[0].getElementsByClassName("el-button")[0].getElementsByTagName('span')[0]

            ){

            var l_content = document.getElementsByClassName("el-calendar__header")[1].getElementsByClassName("el-calendar__button-group")[0].getElementsByClassName("el-button")[0].getElementsByTagName('span')[0];

            var l_value = l_content.innerText;

            l_value = '<div class="calendar_symbol_l">‹</div>';

            l_content.innerHTML = l_value;

        }

        // el-calendar__button-group bnt2   ›

        if (document.getElementsByClassName("el-calendar__header") && document.getElementsByClassName("el-calendar__header")[1] &&

            document.getElementsByClassName("el-calendar__header")[1].getElementsByClassName("el-calendar__button-group")[0] && 

            document.getElementsByClassName("el-calendar__header")[1].getElementsByClassName("el-calendar__button-group")[0].getElementsByClassName("el-button")[2].getElementsByTagName('span')[0]

          ){

            var r_content = document.getElementsByClassName("el-calendar__header")[1].getElementsByClassName("el-calendar__button-group")[0].getElementsByClassName("el-button")[2].getElementsByTagName('span')[0];

            var r_value = r_content.innerText;

            r_value = '<div class="calendar_symbol_l">›</div>';

            r_content.innerHTML = r_value;

          }

      },

      // 针对url路径进行参数处理
      // 'http://localhost:3007/src/table2-1/index.shtml#
      //  ?cate_type=1&cate_date=20230628&paramid=pm&cate=cu';
      analysisUrl: function analysisUrl() {
        //console.log(window.location.href);
        var url = window.location.href.includes('?') ? window.location.href.split('?')[1] : ''; //截取？后面的内容
        if (url == '') {
          return false;
        }
        var paramsArr = url.split('&'); //第一次分割
        var paramsObj = {};
        for (var i = 0; i < paramsArr.length; i++) {
          var combina = paramsArr[i].split('='); //第二次分割
          paramsObj[combina[0]] = combina[1];
        }
        return paramsObj;
      },

    }
  });
})();