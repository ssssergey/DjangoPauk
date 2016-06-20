'use strict';

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
            $itemsFactory.getCountries().query(
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
            $itemsFactory.getCountries().query(
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
    .controller('DocxController', ['$scope', '$stateParams', '$http',
        function ($scope, $stateParams, $http) {
            $scope.download_docx = function (e, country_name, country_slug) {
            //    $itemsFactory.download().get({country_name: country_name, country_slug: country_slug})
            //    .$promise.then(
            //    function (response) {
            //        $scope.item = response;
            //        console.log($scope.item);
            //    },
            //    function (response) {
            //        $scope.message = "Ошибка: " + response.status + " " + response.statusText;
            //    }
            //);

                //$.get('/api/generate_docx/?name=' + country_name + '&slug=' + country_slug, function(data){
                //    console.log(data)
                //});

                //$http.get('/api/generate_docx/?name=' + country_name + '&slug=' + country_slug, {
                //    responseType: 'arraybuffer', headers: {
                //        'Content-Type': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
                //    }
                //})
                //    .then(function (data, status, headers, config) {
                //        $scope.count = data['headers']('Count');
                //        console.log($scope.count);
                //        var country = e.currentTarget.innerHTML;
                //        e.currentTarget.innerHTML = 'Скачано ' + $scope.count;
                //        setTimeout(function () {
                //            e.currentTarget.innerHTML = country
                //        }, 2000);
                //    }, function (response) {
                //        // called asynchronously if an error occurs
                //        // or server returns response with an error status.
                //    });
            };
        }
    ]);

