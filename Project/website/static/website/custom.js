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
            url: "/getnumbers/",
            success: function (response) {
                for (var i = 0; i < 4; i++) {

                    temp = document.createElement("div")
                    $(temp).addClass('gamebg')




                    details = document.createElement("div")
                    $(details).addClass(`gamebgheader`)
                    span1 = document.createElement('span')
                    span2 = document.createElement('span')
                    $(span2).addClass(`gamebgheader${i}`)
                    $(span1).attr('id', `gamebgheader${i}`)
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

                    amount = "<div class='row'>" + `<div class='col-6'><h5 class='amt'>AMOUNT:</h5></div>` + `<div class='col-6'><input type='number' id='amount${i}'></div>`
                    $(temp).append(amount)

                    btn = "<span class='btn-border w-100 mt-2 mb-3'>" + `<button class='cmn-btn w-100 submit'  id='submit${i}'>` + 'Submit'
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
                            $(".gamebgheader0").text(`wk${time[0].week}`)
                            var timebox = document.getElementById("gamebgheader0")
                            const timer = setInterval(function () {
                                const end = Date.parse(time[0].expire)
                                const now = new Date().getTime()
                                const diff = end - now

                                const minutes = Math.floor((end / (1000 * 60) - (now / (1000 * 60))) % 60)
                                const seconds = Math.floor((end / (1000) - (now / (1000))) % 60)

                                let DisplayMinutes
                                let DisplaySeconds

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
                                    timebox.innerHTML = `${DisplayMinutes}:${DisplaySeconds}`
                                }
                                else {
                                    clearInterval(timer)
                                    $.ajax({
                                        type: 'POST',
                                        url: '/create/',
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

                            $("#submit0").on('click', function () {
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
                                    var inp_amount = parseInt($('#amount0').val())
                                    var bal = parseInt($('.bal').text())

                                    if (bal > inp_amount) {
                                        if (inp_amount >= 100){
                                            $.ajax({
                                                type: "POST",
                                                url: "/datasubmit/",
                                                data: {
                                                    list,
                                                    week: wk,
                                                    amount: $('#amount0').val()
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
                                        else{
                                            swal("Minimum stake is ₦100"); 
                                        }
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
                        /* index for div two.....*/
                        if ($(temp).index() === 1) {
                            var index = $(this).index()
                            var wk = `${time[1].week}`
                            $(".gamebgheader1").text(`wk${time[1].week}`)
                            var timebox1 = document.getElementById("gamebgheader1")
                            const timer = setInterval(function () {
                                const end = Date.parse(time[1].expire)
                                const now = new Date().getTime()
                                const diff = end - now

                                const minutes = Math.floor((end / (1000 * 60) - (now / (1000 * 60))) % 60)
                                const seconds = Math.floor((end / (1000) - (now / (1000))) % 60)

                                let DisplayMinutes
                                let DisplaySeconds

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
                                    timebox1.innerHTML = `${DisplayMinutes}:${DisplaySeconds}`
                                }
                                else {
                                    clearInterval(timer)
                                    $.ajax({
                                        type: 'POST',
                                        url: '/create/',
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
                            $("#submit1").on('click', function () {
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
                                    var inp_amount = parseInt($('#amount1').val())
                                    var bal = parseInt($('.bal').text())

                                    if (bal > inp_amount) {
                                        if (inp_amount >= 100){
                                            $.ajax({
                                                type: "POST",
                                                url: "/datasubmit/",
                                                data: {
                                                    list,
                                                    week: wk,
                                                    amount: $('#amount1').val()
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
                                        else{
                                            swal("Minimum stake is ₦100"); 
                                        }
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
                                    $(".picks:eq(1)").append(ball)
                                }
                                else {
                                    swal({
                                        title: "Numbers of picks exceeded",
                                        text: "click on the a ball to replace"
                                    })
                                }
                            });
                        }
                        /* ending for index two */
                        /*Beginning for index three */
                        if ($(temp).index() === 2) {
                            var index = $(this).index()
                            var wk = `${time[2].week}`
                            $(".gamebgheader2").text(`wk${time[2].week}`)
                            var timebox2 = document.getElementById("gamebgheader2")
                            const timer = setInterval(function () {
                                const end = Date.parse(time[2].expire)
                                const now = new Date().getTime()
                                const diff = end - now

                                const minutes = Math.floor((end / (1000 * 60) - (now / (1000 * 60))) % 60)
                                const seconds = Math.floor((end / (1000) - (now / (1000))) % 60)

                                let DisplayMinutes
                                let DisplaySeconds

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
                                    timebox2.innerHTML = `${DisplayMinutes}:${DisplaySeconds}`
                                }
                                else {
                                    clearInterval(timer)
                                    $.ajax({
                                        type: 'POST',
                                        url: '/create/',
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
                                    window.location.reload(true)
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
                            $("#submit2").on('click', function () {
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
                                    var inp_amount = parseInt($('#amount2').val())
                                    var bal = parseInt($('.bal').text())

                                    if (bal > inp_amount) {
                                        if (inp_amount >= 100){
                                            $.ajax({
                                                type: "POST",
                                                url: "/datasubmit/",
                                                data: {
                                                    list,
                                                    week: wk,
                                                    amount: $('#amount2').val()
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
                                        else{
                                            swal("Minimum stake is ₦100"); 
                                        }
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
                                    $(".picks:eq(2)").append(ball)

                                }
                                else (
                                    swal({
                                        title: "Numbers of picks exceeded",
                                        text: "click on the a ball to replace"
                                    })
                                )
                            });
                        }
                        /*ending for index three */

                        /*Beginning for index four */
                        if ($(temp).index() === 3) {
                            var index = $(this).index()
                            var wk = `${time[3].week}`
                            $(".gamebgheader3").text(`wk${time[3].week}`)
                            var timebox3 = document.getElementById("gamebgheader3")
                            const timer = setInterval(function () {
                                const end = Date.parse(time[3].expire)
                                const now = new Date().getTime()
                                const diff = end - now

                                const minutes = Math.floor((end / (1000 * 60) - (now / (1000 * 60))) % 60)
                                const seconds = Math.floor((end / (1000) - (now / (1000))) % 60)

                                let DisplayMinutes
                                let DisplaySeconds

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
                                    timebox3.innerHTML = `${DisplayMinutes}:${DisplaySeconds}`
                                }
                                else {
                                    clearInterval(timer)
                                    $.ajax({
                                        type: 'POST',
                                        url: '/create/',
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
                            $("#submit3").on('click', function () {
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
                                    var inp_amount = parseInt($('#amount3').val())
                                    var bal = parseInt($('.bal').text())

                                    if (bal > inp_amount) {
                                        if (inp_amount >= 100){
                                            $.ajax({
                                                type: "POST",
                                                url: "/datasubmit/",
                                                data: {
                                                    list,
                                                    week: wk,
                                                    amount: $('#amount3').val()
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
                                        else{
                                            swal("Minimum stake is ₦100"); 
                                        }
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
                                    $(".picks:eq(3)").append(ball)

                                }
                                else (
                                    swal({
                                        title: "Numbers of picks exceeded",
                                        text: "click on the a ball to replace"
                                    })
                                )
                            });
                        }
                        /* ending for index four */

                    })
                }

            },
            error: function (error) {
                console.log(error)
            }
        });
        /* Virtual Games Result collection */
        $.ajax({
            type: 'GET',
            url: '/results/',
            success: function (response) {

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


