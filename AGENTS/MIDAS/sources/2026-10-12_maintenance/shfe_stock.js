/** li.pengyang-v1.0.0 APP License By  */
;'use strict';

/*
 * @Description: 
 * @Author: zhou.xiaowei@trs.com.cn
 * @Date: 2023-09-07 16:30:59
 */
Vue.component("weekly-stock-table-component", {
  template: '#weeklystock-component',
  props: {
    current_date: {
      type: String,
      default: ''
    },
    side_type_select: {
      type: String,
      default: ''
    },
    productionClass: {
      type: String,
      default: 'all'
    }
  },
  watch: {
    current_date: {
      handler: function handler(newVal, oldVal) {
        var _this = this;

        this.type_select = 'all';
        this.queryTableData_weeklystock();
      }
    },
    isShowIframeUrl: {
      handler: function handler(newValue, oldValue) {
        if (newValue && this.current_date < this.oldHtmlEndDate) {
          this.handleIframeWidth();
        }
      }
    }
  },
  data: function data() {
    return {
      type_select: 'all',
      showSelect: true,
      loading: false, // 加载状态
      json: {}, // 原始数据
      name: "名字",
      unit_cn: [], // 单位
      data_path: '', // 路径
      isShowReportMemo2: false, // 表格2备注是否显示
      reportMemo2: {}, // 表格2备注
      recordName: [], // 记录每个table下的name
      recordList: [], // 记录每个table下的具体内容
      resultList: [], // 最终的结果数组
      isShowMore1: false, // 备注的展开是否更多
      pro_list1: [], // 第二张表格的数据
      noData: false, // 暂无数据
      isShowOtherTable: false, // 是否显示其他表格
      resultName: [], // 处理完成之后的，每个商品种类的数组
      iframeUrl: '', // iframe路径
      isShowIframeUrl: false, // 是否显示iframe标签
      // 新增参数
      isShowMobilePage: false,
      form: {
        searchCate: 'all',
        searchCateItem: ''
      },
      select_doc: {}, // 新增 记录品类信息
      select_arr1: {}, // 新增 记录大类信息
      select_arr2: {}, // 新增 记录小类信息
      recordCateIndex: 'all', // 新增
	  newhtml:'',
	  oldHtmlEndDate:'20140519',

    };
  },
  mounted: function mounted() {
    // 新增
    if (screenWidth < 750) {
      this.isShowMobilePage = true;
    } else {
      this.isShowMobilePage = false;
    }
  },
  methods: {
     // el-table表头强制换行
     renderHeader( h, { column } ) {
      let arr = []
      if( column.label &&  column.label.includes('<br>')  ) {
        let splitArr = column.label.split('<br>')
        splitArr.forEach( item => {
          if(item) {
            arr.push( h('p', {} , item) )
          }
        });
        return h('p', {} , arr)
      } else {
        arr.push( h('p', {} , column.label) )
        return h('p', {} , arr)
      }
    },

    // 新增 金属、能源化工、金属
    handleCateTab: function handleCateTab(value) {
      this.recordCateIndex = value;
      if (value !== 'all') {
        this.form.searchCateItem = this.select_arr2[this.recordCateIndex][0].productid;
      } else {
        this.form.searchCateItem = 'all';
      }
      this.resultList = {};
      this.$nextTick(() => {
        this.getProductionId_info(this.form.searchCateItem);
      })
    },
    // 新增 种类： 铜...
    handleCateItemTab: function handleCateItemTab(value) {
      this.resultList = {};
      this.$nextTick(() => {
        this.getProductionId_info(value);
      })
    },

    // 新增 url携带参数，下拉框赋值处理
    handleselectdefault: function handleselectdefault(side_type_select) {
      let recordItemIndexList = [];
      recordItemIndexList = this.findElementWithPropertyIndex(this.select_arr2, 'productid', side_type_select)
      this.form.searchCate = recordItemIndexList[0];
      this.recordCateIndex = recordItemIndexList[0];
      this.$nextTick(() => {
        this.form.searchCateItem = side_type_select;
      });
    },
    // 新增
    findElementWithPropertyIndex: function findElementWithPropertyIndex(arr, propertyName, propertyValue, parentIndex = []) {
      for (let i = 0; i < arr.length; i++) {
        if (Array.isArray(arr[i])) {
          // 如果当前元素是数组，则递归调用
          const result = findElementWithPropertyIndex(arr[i], propertyName, propertyValue, [...parentIndex, i]);
          if (result !== null) {
            return result;
          }
        } else if (typeof arr[i] === 'object' && arr[i] !== null) {
          // 如果当前元素是对象，检查它的属性
          if (arr[i][propertyName] === propertyValue) {
            // 如果找到具有特定属性值的对象，返回当前下标和所属上一层数组的下标
            return [...parentIndex, i];
          }
        }
      }
      return null; // 如果没有找到具有特定属性值的对象，返回null
    },


    queryTableData_weeklystock() {
	 
      this.noData = false;
      this.loading = true;

      this.type_select = 'all';
      this.showSelect = false;
      this.$nextTick(function () {
        this.showSelect = true;
      });
	 
	 
	  this.newhtml=''
	  
	  
      
      this.isShowIframeUrl = false;
      
      var vm = this;
      if (this.current_date < this.oldHtmlEndDate) {
        this.iframeUrl = api_future_weeklystock_html(this.current_date);
        $.ajax({
          type: "GET",
          url: api_future_weeklystock_html(this.current_date),
          complete: function complete(response) {
            vm.loading = false;
            // vm.iframeUrl = response.responseText;
            if (response.status != 404) {
              vm.isShowIframeUrl = true;
            } else {
              // 没有数据
              vm.loading = false;
              vm.noData = true;
              vm.isShowIframeUrl = false;
            }
          },
          error: function error() {
            // 没有数据
            vm.loading = false;
            vm.noData = true;
          }
        });
      } else {
        // 报表数据查询
		if (vm.side_type_select) {
		vm.type_select=	vm.side_type_select;
		}

		vm.query_iframe_html();
		
       
      }
    },
	query_iframe_html(){
		var vm = this;
		 vm.isShowIframeUrl = true;
		 vm.loading = true;
		 vm.noData = false;
		 vm.newhtml=''
		var code=vm.type_select.split('_')[0];
		var exchangeid=getProductProp(vm.side_type_select, 'exchangegroupid');
		vm.iframeUrl =api_weeklystock_iframe(vm.current_date,code,exchangeid);
		$.ajax({
		  type: "GET",
		  url: vm.iframeUrl,
		  dataType:'html',
		  complete: function complete(response) {
		    if (response.status != 404) {
				setTimeout(function(){vm.loading = false;},500)
				
		      vm.isShowIframeUrl = true;
			   //vm.handleIframeWidth();
			   vm.adjustIframe(response.responseText)
			   
		    } else {
		      // 没有数据
		      vm.loading = false;
		      vm.noData = true;
		      vm.isShowIframeUrl = false;
			  vm.query_dat_stock(); 
		    }
		  }
		});
	},
	query_dat_stock(){
		var vm = this;
		 vm.loading = true;
		 vm.noData = false;
		 vm.isShowIframeUrl=false
		$.ajax({
		  url: api_future_weeklystock(this.current_date),
		  dataType: 'json',
		  success: function success(json) {
		    vm.loading = false;
		    //  没有数据的情况
		    if (json.o_cursor.length === 0) {
		      vm.noData = true;
		      return;
		    }
		    vm.json = json;
		    if (vm.side_type_select) {
		      vm.getProductionId_info(vm.side_type_select);
		      return;
		    }
		   
		    // 针对表格数据进行处理
		    vm.handleJsonData();
		  },
		  error: function error() {
		    // 没有数据
		    vm.loading = false;
		    vm.noData = true;
		  }
		});
	},
    
	getProductionId_info(id) {
      this.type_select = id;
	  if(this.isShowIframeUrl){
	  		 this.query_iframe_html(); 
	  }else{
	  		this.handleJsonData( this.type_select);
	  }
      
    },

    isExpand(type) {
      if (type == '2') {
        this.isShowMore2 = !this.isShowMore2;
      }
    },

    rowClassName(_ref) {
      var row = _ref.row,
        rowIndex = _ref.rowIndex,
        columnIndex = _ref.columnIndex;

      if (row.TYPE_LINE) {
        return "special_row_type";
      }
      if (row.isTotal) {
        return "isTotal tdBorder";
      }
  
      if (rowIndex !== 0) {
        return 'tdBorder';
      }
    },

    handleJsonData() {
      var _this2 = this;
		if (this.type_select === 'all') {
		  this.isShowOtherTable = true;
		} else {
		  this.isShowOtherTable = false;
		}
      var tableData = JSON.parse(JSON.stringify(this.json));
      // 第一张表格的数据
      if( tableData.o_cursor && tableData.o_cursor.length > 0 ) {
        tableData.o_cursor.forEach(function (item, index) {
          if (index === 0) {
            item.isFuFirst = true;
          }
          item.isShowFuFir = true
        });
      }
      var pro_list = tableData.o_cursor; // 上期品种
      // 能源品种
      if( tableData.o_cursorine && tableData.o_cursorine.length > 0 ) {
        tableData.o_cursorine.forEach(function (item, index) {
          if (index === 0) {
            item.isIneFirst = true;
          }
          item.isShowIneFir = true
          pro_list.push(item);
        });
      }
      if( tableData.o_cursorfu && tableData.o_cursorfu.length > 0 ) {
          // 燃料油
        tableData.o_cursorfu.forEach(function (item, index) {
          item.isShowFuFir = true
          pro_list.push(item);
        });
      }
      var tableData3 = tableData.o_cursorau && tableData.o_cursorau.length > 0 ?  tableData.o_cursorau : []  ; // 黄金
      // 将数组分为多产品数组
      var only_info1 = listParamsRepeat(tableData.o_cursor, 'VARNAME');
      // 针对数组进行的保留小数点位数precision---字段的添加
      // pro_precision(only_info, 'decimal_number');
      this.unit_cn = getWebConfigPropValue('weightunits_en');
      this.recordName = [];
      this.recordList = [];
      this.resultList = [];
      this.resultName = [];
      var pro_config_week = JSON.parse(sessionStorage.getItem('pro_config'));
      var only_info = [];
      // 品种查询
      if (this.type_select !== 'all') {
        only_info = only_info1.filter(function (item, index) {
          var productionId = '';
          var cate_name1 = '';
          if (item.VARID) {
            let  varId = getProductByGroup(item.VARID, '1') ;
            return varId === _this2.type_select;
          } else {
            Object.keys(pro_config_week).forEach(function (o) {
              var isWarehouseAndfactory = item.VARNAME.includes('仓库') || item.VARNAME.includes('厂库') ? (item.VARNAME.includes('(') ? item.VARNAME.split('(')[0] :  item.VARNAME ) : item.VARNAME;
              var cate_name = isWarehouseAndfactory.includes('$$') ? isWarehouseAndfactory.split('$$')[0] : isWarehouseAndfactory;
              let str_item = cate_name;
              if( str_item.includes('仓库') ) {
                cate_name = str_item.split('仓库')[0];
              } else if(str_item.includes('厂库')) {
                cate_name = str_item.split('厂库')[0];
              }
              if (cate_name === '铜') {
                productionId = 'cu_f';
              } else if (cate_name === '铜(BC)') {
                productionId = 'bc_f';
              } else if (cate_name === '铝') {
                productionId = 'al_f';
              } else if (cate_name === '氧化铝') {
                productionId = 'ao_f';
              }  else if (cate_name === '燃料油') {
                productionId = 'fu_f';
              } else if (cate_name === '低硫燃料油') {
                productionId = 'lu_f';
              } else {
                if (o.includes(enumObj.productclass_f) && (cate_name === pro_config_week[o].stock_name_cn || pro_config_week[o].stock_name_cn && pro_config_week[o].stock_name_cn.includes(cate_name))) {
                  productionId = o;
                }
              }
            });
            return productionId === _this2.type_select;
          }
        });

        if( only_info && only_info.length == 0 ) {
          this.noData = true;
        }
      } else {
        only_info = only_info1;
      }
      // 针对的是上海期货交易所指定交割仓库期货仓单日报的表格处理
      only_info.forEach(function (item, index) {
        if( index == 0 && this.type_select !== 'all' ) {
          if( item.isShowIneFir ) {
            item.isShowIneReport = true
          }
          if( item.isShowFuFir ) {
            item.isShowFuReport = true
          }
        }
        var style_warehouse_type = '';
        var style_factory_type = '';
        var productionId = '';
        if (item.VARID) {
          productionId = getProductByGroup(item.VARID, '1') ;
          style_warehouse_type = pro_config_week[productionId].weekly_warehouse_type ? pro_config_week[productionId].weekly_warehouse_type : '';
          style_factory_type = pro_config_week[productionId].weekly_factory_type ? pro_config_week[productionId].weekly_factory_type : '';
        } else {
          Object.keys(pro_config_week).forEach(function (o) {
            var isWarehouseAndfactory = item.VARNAME.includes('仓库') || item.VARNAME.includes('厂库') ? (item.VARNAME.includes('(') ? item.VARNAME.split('(')[0] :  item.VARNAME ) : item.VARNAME;
            var cate_name = isWarehouseAndfactory.includes('$$') ? isWarehouseAndfactory.split('$$')[0] : isWarehouseAndfactory;
            let str_item = cate_name;
            if( str_item.includes('仓库') ) {
              cate_name = str_item.split('仓库')[0];
            } else if(str_item.includes('厂库')) {
              cate_name = str_item.split('厂库')[0];
            } 
            if (cate_name === '铜') {
              productionId = 'cu_f';
            } else if (cate_name === '铜(BC)') {
              productionId = 'bc_f';
            } else if (cate_name === '铝') {
              productionId = 'al_f';
            } else if (cate_name === '氧化铝') {
              productionId = 'ao_f';
            }  else if (cate_name === '燃料油') {
              productionId = 'fu_f';
            } else if (cate_name === '低硫燃料油') {
              productionId = 'lu_f';
            }  else if (o.includes(enumObj.productclass_f) && (cate_name === pro_config_week[o].stock_name_cn || ( pro_config_week[o].stock_name_cn && pro_config_week[o].stock_name_cn.includes(cate_name) ) )) {
              productionId = o;
            }
          });
          style_warehouse_type = pro_config_week[productionId].weekly_warehouse_type ? pro_config_week[productionId].weekly_warehouse_type : '';
          style_factory_type = pro_config_week[productionId].weekly_factory_type ? pro_config_week[productionId].weekly_factory_type : '';
          if( _this2.current_date < '20181025' && productionId === 'fu_f' ) {
            style_warehouse_type = '3'
            style_factory_type = '3'
          }
        }
        var arrItem = {
          productionId: productionId.split('_')[0],
          REGNAME: item.VARNAME,
          varname: item.VARNAME,
	   isIne:pro_config_week[productionId].exchangegroupid==='ine'?true:false,
          WHSTOCKCHANGE: 'Unit: ' + _this2.unit_cn[item.WGHTUNIT],
          style_warehouse_type: style_warehouse_type,
          style_factory_type: style_factory_type,
          isShowReportMemo: false, // 每个表格是否显示备注
          propvalue: [], // 每个表格备注内容,可能存在多个
          TYPE_LINE: true // 首行商品名称的标识
        };


        var stock_depot_name_en = pro_config_week[productionId] ? pro_config_week[productionId].stock_depot_name_en : '' ;
        if (item.WHTYPE === '2') {
          // arrItem.titleName = '交割厂库'; stock_depot_name_en
          arrItem.titleName =stock_depot_name_en? 'Factory Depot' : 'Factory Warehouse';
          arrItem.table_style = arrItem.style_factory_type;
          arrItem.isSpecial = stock_depot_name_en ? true: false;

        } else {
          if( item.VARNAME.includes('厂库') ) {
            arrItem.titleName =stock_depot_name_en? 'Factory Depot' : 'Factory Warehouse';
            arrItem.table_style = arrItem.style_factory_type;
            arrItem.isSpecial = stock_depot_name_en ? true: false;
          } else if (item.VARNAME.includes('仓库')) {
            // arrItem.titleName = '交割仓库';
            arrItem.titleName =stock_depot_name_en? 'Depot' : 'Warehouse';
            arrItem.isSpecial = stock_depot_name_en ? true: false;
            arrItem.table_style = arrItem.style_warehouse_type;
          } else {
            arrItem.titleName =stock_depot_name_en? 'Depot' : 'Warehouse';
            arrItem.isSpecial = stock_depot_name_en ? true: false;
            arrItem.table_style = arrItem.style_warehouse_type;
          }
        }

        // 筛选的时候上期品种备注
        if( item.isShowFuFir && item.isShowFuReport &&  _this2.type_select !== 'all'  ) {
          var recordFirstMemo = getReportMemo('shfe_weeklystock', enumObj.report_1_note_total, _this2.current_date);
          if (recordFirstMemo.propvalue) {
            arrItem.isShowReportMemo = true;
            arrItem.propvalue.push(recordFirstMemo.propvalue);
          }
        }
        // 筛选的时候能源品种备注
        if( item.isShowIneFir && item.isShowIneReport &&  _this2.type_select !== 'all' ) {
          var recordFirstMemo = getReportMemo('shfe_weeklystock', enumObj.report_2_note_total, _this2.current_date);
          if (recordFirstMemo.propvalue) {
            arrItem.isShowReportMemo = true;
            arrItem.propvalue.push(recordFirstMemo.propvalue);
          }
        }
      
        if (item.isIneFirst ) {
          if( _this2.type_select === 'all' ) {
            var recordFirstMemo = getReportMemo('shfe_weeklystock', enumObj.report_2_note_total, _this2.current_date);
            if (recordFirstMemo.propvalue) {
              arrItem.isShowReportMemo = true;
              arrItem.propvalue.push(recordFirstMemo.propvalue);
            }
          }
        }


        if (item.isFuFirst ) {
          if( _this2.type_select === 'all' ) {
            var _recordFirstMemo = getReportMemo('shfe_weeklystock', enumObj.report_1_note_total, _this2.current_date);
            if (_recordFirstMemo.propvalue) {
              arrItem.isShowReportMemo = true;
              arrItem.propvalue.push(_recordFirstMemo.propvalue);
            }
          }
        }

        var reportMemo = {};
        if (arrItem.table_style === '6') {
          reportMemo = getReportMemo('shfe_weeklystock', 'week_stock_' + arrItem.productionId + '_2', _this2.current_date);
        } else {
          reportMemo = getReportMemo('shfe_weeklystock', 'report_1_note_product_' + arrItem.productionId, _this2.current_date);
        }
        // // table1备注 report_3_note_total
        if (reportMemo.propvalue) {
          arrItem.isShowReportMemo = true;
          arrItem.propvalue.push(reportMemo.propvalue);
        }

        _this2.recordName.push(arrItem);
        var recordListItem = [];
        pro_list.forEach(function (m) {
          if (m.VARNAME.trim() === item.VARNAME.trim()) {
            if (m.VARNAME.trim() === '黄金$$GOLD') {
              tableData3.forEach(function (a) {
                recordListItem.push(a);
              });
            } else {
              recordListItem.push(m);
            }
          }
        });
        _this2.recordList.push(recordListItem);
      });

      // // 针对首行商品名称做处理
      this.recordList.forEach(function (item, index) {
        item.unshift(_this2.recordName[index]);
      });


      var pattTotal = new RegExp(enumObj.field_key_all_total);
      var pattTotal_2 = new RegExp(enumObj.field_key_total);
      var pattTotal_3 = new RegExp(enumObj.field_key_bonded_all_total);
      var pattTotal_4 = new RegExp(enumObj.field_key_pay_tax_all_total);

      this.recordList.forEach(function (item, index) {
        var regname = ''; // 每一项原始名字为空
        if (_this2.recordName[index].varname !== '黄金$$GOLD') {
          item.forEach(function (m) {
            var zj = m.WHABBRNAME && m.WHABBRNAME.includes('$$') ? m.WHABBRNAME.split('$$')[0] : m.WHABBRNAME;
            if (pattTotal.test(zj) || pattTotal_2.test(zj) || pattTotal_3.test(zj) || pattTotal_4.test(zj)) {

              if (pattTotal_2.test(zj) && (_this2.recordName[index].table_style === '4' || _this2.recordName[index].table_style === '5')) {
                // 针对 品级、油种，表格中的合计单元格做合并的标识
                m.isNeedcolSpan = true;
              }
              // 针对总计、合计、保税总计、完税总计做特殊样式的标识
              m.isTotal = true;
            }
            if ( m.REGNAME == '' || m.REGNAME == null || regname != m.REGNAME.split('$$')[0]) {
              if( m.REGNAME == null ) {
                regname = ''
              } else {
                regname = m.REGNAME.split('$$')[0];
              }
              if (pattTotal.test(zj) || pattTotal_3.test(zj) || pattTotal_4.test(zj)) {
                m.colSpan = 2;
                m.rowSpan = 0;
                m.isTotalSpan = true;
              } else {
                m.rowSpan = m.WHROWS;
                m.colSpan = 0;
              }
            } else {
              m.colSpan = 0;
              m.rowSpan = 0;
            }
          });
        }
      });

      this.$nextTick( () => {
        this.resultName = this.recordName;
        this.resultList = this.recordList;
      } )

      // 第二张报表
      this.pro_list1 = tableData.o_cursormonwrtexpr; // 标准仓单到期数量
      if (this.pro_list1.length == 0) {
        this.isShowOtherTable = false; // 是否显示 标准仓单到期数量
      }
      // 第二张报表 备注
      this.reportMemo2 = getReportMemo('shfe_weeklystock', enumObj.report_3_note_total, this.current_date);
      // table1备注 report_3_note_total
      if (this.reportMemo2.propvalue) {
        this.isShowReportMemo2 = true;
      }
    },

    arraySpanMethod(_ref2) {
      var row = _ref2.row,
      column = _ref2.column,
      rowIndex = _ref2.rowIndex,
      columnIndex = _ref2.columnIndex,
      index = _ref2.index;
      var rowItem = row.rowSpan;
      if (columnIndex == 0) {
        

        if (rowIndex !== 0 && rowItem !== 0) {
          if (row.isTotalSpan) {
            return {
              rowspan: 0,
              colspan: 0
            };
          }
          return {
            rowspan: rowItem,
            colspan: 1
          };
        } else {
          if (rowItem == 0) {
            return {
              rowspan: 0,
              colspan: 0
            };
          } else {
            if( rowIndex == 0 ) {
              return {
                rowspan: 1,
                colspan: 2
              };
            } else {
              return {
                rowspan: 1,
                colspan: 1
              };
            }

            
          }
        }
      }
      if (columnIndex === 1) {
        if( rowIndex == 0 ) {
          return {
            rowspan: 0,
            colspan: 0
          }
        }
        if (row.isTotalSpan) {
          return {
            rowspan: 1,
            colspan: 2
          };
        }
        if (row.isNeedcolSpan) {
          return {
            rowspan: 1,
            colspan: 2
          };
        }
      }
      if (columnIndex === 2) {
        if (row.isNeedcolSpan) {
          return {
            rowspan: 0,
            colspan: 0
          };
        }
      }
    },

    handleIframeWidth() {
      this.$nextTick(function () {
        document.getElementById('iframe-part').onload = function () {
          //加载完成
          let width_box = '1024px';
          let line_height_box = '24px';
          if (screenWidth > 750) {
            width_box = '1024px';
            line_height_box = '24px';
          } else {
            width_box = '3.45rem';
            line_height_box = 'unset';
          }
          document.getElementById('iframe-part') //获取到iframe
          .contentWindow //获取到iframe的window
          .document //获取到iframe的document
          .getElementsByTagName('table')[0] //正常获取元素
          .style.width = width_box; //修改样式
          document.getElementById('iframe-part').contentWindow.document.getElementsByClassName('article-detail-text')[0].style.lineHeight = line_height_box;
        };
      });
    },
	//获取html内容
	adjustIframe(data) {
		let vm=this;
		var doc=new DOMParser().parseFromString(data,'text/html');
		var content=doc.body.innerHTML;
		this.$nextTick(()=>{
			if(this.$refs.container){
			this.$refs.container.innerHTML=content;	
			}
		})
		vm.newhtml=content;	
		
		
		/* var ifr = document.getElementById("iframe-part");
		  var iDoc = ifr.contentWindow;
		  var html=iDoc.document.getElementById('stock').innerHTML;
		  vm.newhtml=html; */
	   },
    
    print_info:function print_info(id){
      // statisticalUtils.js 公共打印方法
      OrgPrintFn(id);
    },

    // 导出excell和txt
    exportExcel(name, type, id) {
      exportExcel(name, type, id);
    }
  },
});