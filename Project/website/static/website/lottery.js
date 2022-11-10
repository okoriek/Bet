$(document).ready(function () {
    var balls
    var temp, btn
    var details, span1, span2
    var picks, amount, value, wks
    var data, time
    var Getdata




    /* Creating and Getting Virtual Games */
    Getdata = function () {
        $.ajax({
            type: "GET",
            url: "/lotterygetnumbers/",
            success: function (response) {


                temp = document.createElement("div")
                $(temp).addClass('gamebg')




                details = document.createElement("div")
                $(details).addClass(`gamebgheader`)
                span1 = document.createElement('span')
                span2 = document.createElement('span')
                $(span2).addClass(`gamebgheaderlot`)
                $(span1).attr('id', `gamebgheaderlot`)
                details.append(span1, span2)
                $(temp).append(details)

                data = response.data
                time = response.time



                data.forEach(function (nums) {
                    balls = "<button class='unclicked sphere'>" + "<center><h3 class='text'>" + nums.value
                    $(temp).append(balls)
                })

                picks = `<div type='text' class="picks sphere" id="1">`
                $('#gamebg').append(temp)
                $(temp).append(picks)


                btn = "<span class='btn-border w-100 mt-2 mb-3'>" + `<button class='cmn-btn w-100 submit'  id='submit'>` + 'Submit'
                $(temp).append(btn)



                $("button.unclicked").each(function () {
                    var colors = 'rgba(' +
                        (Math.floor((225 - 0) * Math.random())) + ',' +
                        (Math.floor((225 - 0) * Math.random())) + ',' +
                        (Math.floor((225 - 0) * Math.random()))
                        + ')';
                    $(this).css("background-color", colors)
                })


                $(temp).each(function (index, element) {
                    /* index for div one.....*/
                    if ($(temp).index() === 0) {
                        var index = $(this).index()
                        var wk = `${time[0].week}`

                        $(".gamebgheaderlot").text(`wk${time[0].week}`)
                        var timebox = document.getElementById("gamebgheaderlot")
                        const timer = setInterval(function () {
                            const end = Date.parse(time[0].expire)
                            const now = new Date().getTime()
                            const diff = end - now


                            const days = Math.floor((end / (1000 * 60 * 60 * 24) - (now / (1000 * 60 * 60 * 24))))
                            const hours = Math.floor((end / (1000 * 60 * 60) - (now / (1000 * 60 * 60))) % 24)
                            const minutes = Math.floor((end / (1000 * 60) - (now / (1000 * 60))) % 60)
                            const seconds = Math.floor((end / (1000) - (now / (1000))) % 60)


                            let DisplayDays
                            let DisplayHours
                            let DisplayMinutes
                            let DisplaySeconds

                            if (days.toString().length < 2) {
                                DisplayDays = '0' + days
                            }
                            else {
                                DisplayDays = days
                            }

                            if (hours.toString().length < 2) {
                                DisplayHours = '0' + hours
                            }
                            else {
                                DisplayHours = hours
                            }

                            if (minutes.toString().length < 2) {
                                DisplayMinutes = '0' + minutes
                            }
                            else {
                                DisplayMinutes = minutes
                            }
                            if (seconds.toString().length < 2) {
                                DisplaySeconds = '0' + seconds
                            }
                            else {
                                DisplaySeconds = seconds
                            }
                            if (diff > 0) {
                                timebox.innerHTML = `${DisplayDays}d:${DisplayHours}h:${DisplayMinutes}m:${DisplaySeconds}s`
                            }
                            else {
                                clearInterval(timer)
                                $.ajax({
                                    type: 'POST',
                                    url: '/lotteryverify/',
                                    data: {
                                        week: wk,
                                    },
                                    success: function (response) {
                                        $(".gamebg").remove()
                                        Getdata()
                                    },
                                    error: function (error) {
                                        console.log(error)
                                    }
                                })
                            }
                        }, 1000)


                        var round = $(this)
                        var count = 0
                        $('.picks').each(function () {
                            $(this).on('click', `.clicked${index}`, function (element) {
                                $(this).remove();
                                count--
                            })
                        });

                        $("#submit").on('click', function () {
                            if (count < 5) {
                                swal('You have to choose 5 number to submit')

                            }
                            else {
                                var list = []
                                var num
                                $(`.clicked${index}`).each(function () {
                                    num = $(this).text()
                                    list.push(num)
                                    $(this).remove()
                                    count = 0
                                })
                                var bal = parseInt($('.bal').text())

                                if (bal >= 500) {
                                    $.ajax({
                                        type: "POST",
                                        url: "/lotterydatasubmit/",
                                        data: {
                                            list,
                                            week: wk
                                        },
                                        success: function (response) {
                                            $('#amount0').val('')
                                            $(".successimg").css('display', 'flex')
                                            $("#successimg").css('display', 'flex')
                                            setTimeout(() => {
                                                $(".successimg").css('display', 'none')
                                                $("#successimg").css('display', 'none')
                                            }, 1600);
                                            $.ajax({
                                                type: "GET",
                                                url: "/getbalance/",
                                                success: function(response){
                                                    $('.bal').text(`${response['balance']}`)
                                                },
                                                error: function(error){
                                                    
                                                }
                                            })
                                        },
                                        error: function (error) {
                                            console.log(error)
                                        }
                                    })
                                }
                                else {
                                    swal("insufficient balance");
                                }
                            }
                        })


                        $(this).on('click', "button.unclicked", function (e) {
                            num = $(e.target).text()
                            if (count < 5) {
                                count++
                                var ball = document.createElement("button")
                                ball.textContent = num
                                $(ball).addClass(`clicked${index}`)
                                $(".picks:eq(0)").append(ball)
                            }
                            else (
                                swal({
                                    title: "Numbers of picks exceeded",
                                    text: "click on the a ball to replace"
                                })
                            )
                        });
                    }
                })


            },
            error: function (error) {
                console.log(error)
            }
        });
        /* Lottery Result collection */
        $.ajax({
            type: 'GET',
            url: '/lotteryresults/',
            success: function (response) {
                console.log(response)

                const results = response.data
                var wk = results[0].week
                wks = `<span class='wk'>wk${wk}:</span>`
                $("#result").append(wks)


                results[0].result.forEach(function (num) {
                    value = "<span class=' result sphere'>" + num
                    $("#result").append(value)
                })

                $("span.result").each(function () {
                    var colors = 'rgba(' +
                        (Math.floor((225 - 0) * Math.random())) + ',' +
                        (Math.floor((225 - 0) * Math.random())) + ',' +
                        (Math.floor((225 - 0) * Math.random()))
                        + ')';
                    $(this).css("background-color", colors)
                })
            },
            error: function (error) {
                console.log(error)

            }
        })
    }
    Getdata()
});


