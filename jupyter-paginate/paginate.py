

import uuid
from IPython.display import display_javascript, display_html, display
import json


html_content='''
<div ng-app="testApp{{{#uuid#}}}">
  <div id="rootElement{{{#uuid#}}}" ng-controller="testController{{{#uuid#}}}">
    <h1>{{title}}</h1>
    
    <div style="height:{{{#domheight#}}}; overflow:scroll;" class="myText{{{#uuid#}}}"></div>

    <div>
        <button
          ng-disabled="currentPage == 0"
          ng-click="currentPage=currentPage-1"
        >
          Previous
        </button>

        Page {{currentPage+1}} of {{numberOfPages()}}

        <button
           ng-disabled="currentPage >= data.length/pageSize - 1"
           ng-click="currentPage=currentPage+1"
        >
          Next
        </button>
    <div>
    
  </div>
</div>
'''

javascript_content='''
//require needs to be configed with the dependencies
require.config({
    paths: {
        velocity: "https://cdn.jsdelivr.net/velocity/1.2.3/velocity.min",
        interact: "https://cdn.jsdelivr.net/interact.js/1.2.6/interact.min",
        angular: "https://cdnjs.cloudflare.com/ajax/libs/angular.js/1.5.8/angular.min"
       },
    shim: {
        'angular': {
            exports: 'angular'
        }
    }
});


require(['angular','jquery'], function(a,$) {
              

      (function(){
        var app = a.module('testApp'+uuid,[]);    
    
        app.controller('testController'+uuid, function($scope){
          $scope.title = title;
          $scope.currentPage = 0;
          $scope.pageSize = 1;
          $scope.data = data;

          $scope.numberOfPages= () => {
            return Math.ceil(
              $scope.data.length / $scope.pageSize
            );
          }


            
          $scope.$watch( "currentPage", function(newVal, oldVal, scope){
              $(".myText"+uuid).html(data[newVal]);
          } );  
            

        });

        app.filter('startFrom', function() {
          return (input, start) => {
            start = +start; //parse to int
            return input.slice(start);
          }
        });
        
        
          
        var el = document.getElementById("rootElement"+uuid);
        if(a.element(el).injector()){
            a.element(el).injector().get('$rootScope').$destroy()
        }  
          
        a.element(document).ready(function() {
                  a.bootstrap(el, ['testApp'+uuid]);
                });        
          
          
      })();
    
    });
'''


class Paginate(object):
    def __init__(self, json_data, title, domheight):
        self.json_str = json.dumps(json_data)
        self.uuid = str(uuid.uuid4()).replace("-","")
        self.title = title
        self.domheight=domheight
        
    def _ipython_display_(self):
        display_html(html_content.replace("{{{#uuid#}}}", self.uuid).replace("{{{#domheight#}}}", self.domheight),
            raw=True
        )

                
        display_javascript("var title="+"'" + self.title + "';\n"+\
                            "var data="+self.json_str+";\n"+\
                           "var uuid='"+self.uuid+"';\n"+\
                           javascript_content , raw=True)
