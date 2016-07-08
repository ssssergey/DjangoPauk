'use strict';

function findAndReplace(object, value, replacevalue) {
  for (var x in object) {
    if (object.hasOwnProperty(x)) {
      if (typeof object[x] == 'object') {
        findAndReplace(object[x], value, replacevalue);
      }
      if (object[x] == value) {
        object["name"] = replacevalue;
        // break; // uncomment to stop after first replacement
      }
    }
  }
}

angular.module('startPage')
    .controller('IndexController', ['$scope', '$stateParams', 'itemsFactory',
        function ($scope, $stateParams, $itemsFactory) {
            //$scope.item = {};
            $scope.showItem = true;
            $scope.message = "Загрузка ...";

        }
    ])
    .controller('ItemsController', ['$scope', '$stateParams', 'itemsFactory',
        function ($scope, $stateParams, $itemsFactory) {
            $scope.showItems = false;
            $scope.message = "Загрузка ...";
            $itemsFactory.getItems().get(
                function (response) {
                    $scope.items = response;
                    console.log($scope.items);
                    $scope.showItems = true;
                },
                function (response) {
                    $scope.message = "Ошибка: " + response.status + " " + response.statusText;
                }
            );
        }
    ])
    .controller('ItemDetailController', ['$scope', '$stateParams', 'itemsFactory',
        function ($scope, $stateParams, $itemsFactory) {
            //$scope.item = {};
            $scope.showItem = false;
            $scope.message = "Загрузка ...";
            //$scope.item =
            $itemsFactory.getItems().get({id: parseInt($stateParams.id, 10)})
                .$promise.then(
                function (response) {
                    $scope.item = response;
                    console.log($scope.item);
                    $scope.showItem = true;
                },
                function (response) {
                    $scope.message = "Ошибка: " + response.status + " " + response.statusText;
                }
            );
        }
    ])
    .controller('CountriesController', ['$scope', '$stateParams', 'itemsFactory',
        function ($scope, $stateParams, $itemsFactory) {
            $scope.showItems = false;
            $scope.message = "Загрузка ...";
            $itemsFactory.getCountryNames().query(
                function (response) {
                    $scope.countries = response;
                    console.log($scope.countries);
                    $scope.showItems = true;
                },
                function (response) {
                    $scope.message = "Ошибка: " + response.status + " " + response.statusText;
                }
            );
        }
    ])
    .controller('CountryListController', ['$scope', '$stateParams', 'itemsFactory',
        function ($scope, $stateParams, $itemsFactory) {
            $scope.showItems = false;
            $scope.message = "Загрузка ...";
            $itemsFactory.getCountryList().get({slug: $stateParams.slug})
                .$promise.then(
                function (response) {
                    $scope.c_items = response;
                    console.log($scope.c_items);
                    $scope.showItems = true;
                },
                function (response) {
                    $scope.message = "Ошибка: " + response.status + " " + response.statusText;
                }
            );
        }
    ])
    .controller('BDController', ['$scope', '$http', '$stateParams', 'itemsFactory',
        function ($scope, $http, $stateParams, $itemsFactory) {
            $scope.showItems = false;
            $scope.message = "Загрузка ...";
            $itemsFactory.atlantCountries().query(
                function (response) {
                    console.log(response);
                    $scope.countries = response;
                    findAndReplace($scope.countries, 'Латинская Америка', 'Лат. Америка')
                    findAndReplace($scope.countries, 'Северный Кавказ', 'Сев. Кавказ')
                    findAndReplace($scope.countries, 'ЮгоВосточная Азия', 'Ю.-В. Азия')
                    $scope.showItems = true;
                },
                function (response) {
                    $scope.message = "Ошибка: " + response.status + " " + response.statusText;
                }
            );

        }
    ]);


