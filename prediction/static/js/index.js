var app = angular.module("avocadoPrediction", []);

app.config(function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
});

app.controller("avocadoPredictionCtrl", function($scope, $http) {
    $scope.predicted_average_price = ""

    $scope.predict = function($this) {
        $http.post('/predict/',
        {
            'sold_plu_4046': $this.predictForm.sold_plu_4046.$modelValue,
            'sold_plu_4225': $this.predictForm.sold_plu_4225.$modelValue,
            'sold_plu_4770': $this.predictForm.sold_plu_4770.$modelValue,
            'small_bags': $this.predictForm.small_bags.$modelValue,
            'large_bags': $this.predictForm.large_bags.$modelValue,
            'xlarge_bags': $this.predictForm.xlarge_bags.$modelValue,
            'organic': $this.predictForm.organic.$modelValue,
            'region': $this.predictForm.region.$modelValue
        })
        .then(function(response) {
            $scope.predicted_average_price = response.data.predicted_average_price;
        });
    }
});