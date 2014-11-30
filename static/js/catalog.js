/**
 * Created by ainurminibaev on 29.11.14.
 */
$(document).ready(function () {
    var page = 0;
    $(".js-catalog").click(function () {
        var $this = $(this);
        if (!$this.hasClass('active')) {
            $(".js-catalog").removeClass('active');
            $this.addClass("active");
            page = 0;
            $("#slider-range").slider("values", min_price, 2 * max_price - max_price / 2);
            catalogAjaxReloader();
        }
    });

    $("#slider-range").slider({
        range: true,
        min: min_price,
        max: 2 * max_price,
        values: [ min_price + 5, 2 * max_price - max_price / 2 ],
        slide: function (event, ui) {
            $("#amount").val("$" + ui.values[ 0 ] + " - $" + ui.values[ 1 ]);
        },
        stop: function (event, ui) {
            catalogAjaxReloader();
        }
    });

    function catalogAjaxReloader() {
        var param_map = {};
        var catalog = $(".js-catalog.active");
        var id = null;
        if (catalog.length) {
            id = parseInt(catalog.data('id'));
            if (id < 0) {
                id = null;
                $("#catalog-title").html("");
            } else {
                $("#catalog-title").html(catalog.text());
            }
        }

        var values = $("#slider-range").slider("values");
        param_map.min_price = values[0];
        param_map.max_price = values[1];

        param_map.catalog = id;
        param_map.page = page
        param_map.csrfmiddlewaretoken = csrf_token;
        $.ajax({
            "method": "POST",
            "url": "/catalog/ajax",
            "data": param_map,
            "success": function (data) {
                var ddiv = $("<div></div>").append(data);
                var goods = ddiv.find(".js-good");
                if (goods.length < 3) {
//TODO hide more btn
                }
                if (page == 0 || goods.length == 0) {
                    $(".js-catalog-body").html(data);
                } else {
                    $(".js-catalog-body").append(data);
                }
                page++;
            },
            "error": function (data) {
                console.log("data loading error");
            }
        });

    }
});

