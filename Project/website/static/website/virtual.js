/* VIRTUAL FOOTBALL GAME SESSSION */
$(document).ready(function () {
    var total

    $.ajax({
        url: '/virtual/fixture/',
        type: 'GET',
        success: function (response) {
            var data = response.data
            var time =  response.time
            var wks =  response.wk
            var i = 1
            var x = 1
            var count = 0
            var timebox = document.querySelector('.countdowntime')
            document.querySelector('.gamewk').innerText = `week ${wks}`
            const timer = setInterval(function () {
    
                const end = Date.parse(time)
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
                    timebox.innerHTML = `00:00`

                    /*
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
                    */
                }
            }, 1000)

            /*
                displaying the odds from the database 
            */

            data.forEach(function (value) {
                var fixture = `<p class='homeaway' id='${i}'>` + value.home_team + ' ' + '-' + ' ' + value.away_team
                $('.teams').append(fixture)
                var home = `<p class='homewin odds' id='${i}'>` + value.home_odd
                $('.home').append(home)
                var draw = `<p class='drawT odds' id='${i}'>` + value.draw_odd
                $('.draw').append(draw)
                var away = `<p class='awaywin odds' id='${i}'>` + value.away_odd
                $('.away').append(away)
                var homeX = `<p class='homedraw odds' id='${i}'>` + value.home_draw_odd
                $('.homeX').append(homeX)
                var awayX = `<p class='awaydraw odds' id='${i}'>` + value.away_draw_odd
                $('.awayX').append(awayX)
                var anybodywin = `<p class='home_away odds' id='${i}'>` + value.home_away_win_odd
                $('.anybodywin').append(anybodywin)
                var gg = `<p class='bts odds' id='${i}'>` + value.bts
                $('.gg').append(gg)
                var ng = `<p class='nbts odds' id='${i}'>` + value.nbts
                $('.ng').append(ng)
                var over2 = `<p class='over_two odds' id='${i}'>` + value.over_two
                $('.over2').append(over2)
                var under2 = `<p class='under_two odds' id='${i}'>` + value.under_two
                $('.under2').append(under2)
                var over3 = `<p class='over_three odds' id='${i}'>` + value.over_three
                $('.over3').append(over3)
                var under3 = `<p class='under_three odds' id='${i}'>` + value.under_three
                $('.under3').append(under3)
                var over4 = `<p class='over_four odds' id='${i}'>` + value.over_four
                $('.over4').append(over4)
                var under4 = `<p class='under_four odds' id='${i}'>` + value.under_four
                $('.under4').append(under4)
                i++
            });

            /* button activated */
            var btn = document.querySelectorAll(`.odds`)
            btn.forEach(function (element) {
                var clicked = false
                var betodd
                var stake



                element.addEventListener('click', function (e) {
                    if (clicked == false) {
                        e.target.style.backgroundColor = 'yellow'
                        e.target.style.color = 'black'
                        var click = e.target.classList.add(`clk`)
                        var teams = document.getElementById(`${e.target.id}`)
                        addclass = e.target.classList.add(`btn${count}`)
                        var fixtures = document.createElement('span')
                        fixtures.classList.add('col-4')
                        fixtures.classList.add('fixtures')
                        var option = document.createElement('span')
                        option.classList.add('col-4')
                        option.classList.add('option')
                        var odds = document.createElement('span')
                        odds.classList.add('col-2')
                        odds.classList.add('gameodds')
                        fixtures.innerHTML = teams.innerHTML
                        option.innerHTML = e.target.parentElement.className
                        odds.innerHTML = e.target.innerHTML
                        var gamecont = document.createElement('div')
                        gamecont.classList.add('containers')
                        var del = document.createElement('i')
                        del.classList.add('col-2')
                        del.classList.add('far')
                        del.classList.add('fa-trash-alt')
                        del.setAttribute('id', `${count}`)

                        /* reset the colour of a button which as been clicked before 
                            removing the odds, alot
                        */

                        del.addEventListener('click', function (d) {
                            var unclk = document.querySelector(`.btn${d.target.id}`)
                            unclk.style.backgroundColor = '#6b21f7'
                            unclk.style.color = 'white'
                            var oddremove = parseFloat(unclk.innerText)
                            var odd = parseFloat(document.querySelector('.total_odd').innerText) / oddremove
                            if (odd.toFixed(2) == 1.00) {
                                console.log(true)
                                document.querySelector('.total_odd').innerText = ` `
                                document.querySelector('.total_amt').innerText = ` `
                            }
                            else {
                                betodd = document.querySelector('.total_odd').innerText = `${odd.toFixed(2)}`
                                stake = parseInt(document.querySelector('.fldinpright').value)
                                total = betodd * stake
                                document.querySelector('.total_amt').innerText = `${total.toFixed(0)}`

                            }


                            d.target.parentElement.remove()


                            clicked = false

                        })
                        /* ended */

                        /* 
                            game bet container for store individual bet
                        */
                        gamecont.setAttribute('id', `btn${count}`)
                        gamecont.append(fixtures, option, odds, del)

                        var content = document.querySelector('.content')
                        content.append(gamecont)

                        var oddn = document.querySelectorAll('.gameodds')
                        var oddcal = []
                        oddn.forEach(function (num) {
                            oddcal.push(parseFloat(num.innerText))
                        })

                        var totalodd = oddcal.reduce(function (total, value) {
                            return total * value
                        }, 1)
                        betodd = document.querySelector('.total_odd').innerText = `${totalodd.toFixed(2)}`
                        stake = parseInt(document.querySelector('.fldinpright').value)
                        total = betodd * stake
                        document.querySelector('.total_amt').innerText = `${total.toFixed(0)}`





                        x++
                        count++
                        clicked = true

                    }
                    else {
                        /* 
                            takes care of all action involving button been unclicked
                            and alot related
                        */

                        e.target.style.backgroundColor = '#6b21f7'
                        e.target.style.color = 'white'
                        var oddremove = parseFloat(e.target.innerText)
                        var odd = parseFloat(document.querySelector('.total_odd').innerText) / oddremove
                        if (odd.toFixed(2) == 1.00) {

                            document.querySelector('.total_odd').innerText = ` `
                            document.querySelector('.total_amt').innerText = ` `
                        }
                        else {

                            betodd = document.querySelector('.total_odd').innerText = `${odd.toFixed(2)}`
                            stake = parseInt(document.querySelector('.fldinpright').value)
                            total = betodd * stake
                            document.querySelector('.total_amt').innerText = `${total.toFixed(0)}`

                        }
                        var last_class = e.target.className.split(' ').pop()

                        unclkbtn = document.querySelector(`#${last_class}`).remove()


                        clicked = false
                    }

                })

            })
        },
        error: function (error) {
            console.log(error)
        }
    })

    /* 
        overlay button for mobile devices and its actions when it is
    */
    var btnbet = document.querySelector('.modalbtn')
    var clickbtn = false
    btnbet.addEventListener('click', function () {
        var betslide = document.querySelector('.bets')
        if (clickbtn == false) {
            console.log('you clicked me')
            betslide.style.display = 'block'
            clickbtn = true
        }
        else {
            console.log('you unclicked me')
            betslide.style.display = 'none'
            clickbtn = false
        }

    })
    /* 
        deals with the amount section i.e amount input field
    */
    var amt = document.querySelector('.fldinpright')
    amt.addEventListener('change', function () {
        var stakes = this.value
        var odd = document.querySelector('.total_odd').innerText
        total = odd * stakes
        document.querySelector('.total_amt').innerText = `${total.toFixed(0)}`


    })

    /* Submitting accumulator games placed */
    var submit = document.getElementById('placebet')
    submit.addEventListener('click', function () {
        var con = document.querySelectorAll('.containers')
        function getRandomNumber(digit) {
            return Math.random().toFixed(digit).split('.')[1];
        }
        var num = getRandomNumber(12);
        console.log(num)
        con.forEach(function (p) {
            var fix = p.querySelector('.fixtures').innerHTML
            var opt = p.querySelector('.option').innerHTML
            var ods = p.querySelector('.gameodds').innerHTML
            console.log(fix + ' ' + opt + ' ' + ods)
            $.ajax({
                url: '/virtual/submitbet/',
                type: 'post',
                data: {
                    'fixtures': fix,
                    'option': opt,
                    'odds': ods,
                    'bet_id': num
                },
                success: function (response) {
                    document.querySelector('.containers').remove()
                    var btn = document.querySelectorAll('.clk')
                    btn.forEach(function (unclick) {
                        unclick.style.backgroundColor = '#6b21f7'
                        unclick.style.color = 'white'
                    })
                },
                error: function (error) {
                    console.log(error)
                }

            })

        })
    })

    // Getting virtual results

    $.ajax({
        url:'/virtual/getvirtualresult/',
        type:'GET',
        success: function(response){
            var results = response.result
            results.forEach(function(val){
                var home = `<span>${val.home}</span><br><br>`
                $('.hometeam').append(home)
                var away = `<span>${val.away}</span><br><br>`
                $('.awayteam').append(away)
                var home_score = `<span>${val.home_score}</span><span class="div">-</span><br><br>`
                $('.home_score').append(home_score)
                var away_score = `<span>${val.away_score}</span><br><br>`
                $('.away_score').append(away_score)
                
            })
        },
        error: function(error){
            console.log(error)
        }
    })

})


