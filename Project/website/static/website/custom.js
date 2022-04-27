$(document).ready(function () {
    var count = 0
    $(".balls").each(function (index, element) {
        $(this).on('click', "button.unclicked", function (e) {
            num = $(e.target).text()
            console.log(num)
            if (count < 5) {
                count++
                var ball = document.createElement("button")
                ball.textContent = num 
                $(ball).addClass('clicked')
                $('#picks').append(ball)
            }
            else (
                alert("Numbers of picks exceeded")
            )
        });
    });
    $('#picks').each(function () {
        $(this).on('click', ".clicked", function (element) {
            var num2 = $(element).text()
            $(this).remove();
            count--
        })
    });
    $.ajax({
        type: "GET",
        url: "/getnumbers/",
        success: function (response) {  
            const data = response.data
            const time = response.time
            temp2 = "<span class='time'>"+"<center>" + time
            $('.gamebgheader').append(temp2)
            data.forEach(function(nums){
                var temp = "<button class='unclicked'>" + "<center><h3 class='text'>" + (nums.value) 
                $("button.unclicked").each(function(){
                    var colors = 'rgba(' + 
                                 (Math.floor((225-0)* Math.random())) + ',' +
                                 (Math.floor((225-0)* Math.random())) + ',' +
                                 (Math.floor((225-0)* Math.random())) 
                    +')';
                    $(this).css("background-color", colors)
                })
                $('.balls').append(temp)
            })
        },
        error : function(error){
            console.log(error)
        }
    });
});













