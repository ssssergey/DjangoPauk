'use strict';
var app = angular.module('startPage', ['ui.router', 'ngResource']);

app.config(function ($interpolateProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
});

app.config(function ($stateProvider, $urlRouterProvider) {
    $stateProvider
        .state('app', {
            url: '/',
            views: {
                'header': {
                    templateUrl: 'static/views/header.html'
                },
                'content': {
                    templateUrl: 'static/views/content.html',
                    controller: 'IndexController'
                },
                'footer': {
                    templateUrl: 'static/views/footer.html'
                }
            }
        })
        .state('app.items', {
            url: 'items',
            views: {
                'content@': {
                    templateUrl: 'static/views/items.html',
                    controller: 'ItemsController'
                }
            }
        })
        .state('app.itemdetails', {
            url: 'items/:id',
            views: {
                'content@': {
                    templateUrl: 'static/views/itemdetail.html',
                    controller: 'ItemDetailController'
                }
            }
        })
        .state('app.countries', {
            url: 'countries',
            views: {
                'content@': {
                    templateUrl: 'static/views/country_select.html',
                    controller: 'CountriesController'
                }
            }
        })
        .state('app.countrylist', {
            url: 'countries/:slug',
            views: {
                'content@': {
                    templateUrl: 'static/views/country_list.html',
                    controller: 'CountryListController'
                }
            }
        })
        .state('app.bd_countries', {
            url: 'bd_countries',
            views: {
                'content@': {
                    templateUrl: 'static/views/bd_country_select.html',
                    controller: 'BDController'
                }
            }
        });
    $urlRouterProvider.otherwise('/');

});


//app.config([
//    '$httpProvider', function ($httpProvider) {
//        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
//        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
//        $http.defaults.headers.post['X-CSRFToken'] = $cookies.csrftoken;
//    }
//]);

