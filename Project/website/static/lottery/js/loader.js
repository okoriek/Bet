////////////////////////////////////////////////////////////
// CANVAS LOADER
////////////////////////////////////////////////////////////

 /*!
 * 
 * START CANVAS PRELOADER - This is the function that runs to preload canvas asserts
 * 
 */
function initPreload(){
	toggleLoader(true);
	
	checkMobileEvent();
	
	$(window).resize(function(){
		resizeGameFunc();
	});
	resizeGameFunc();
	
	loader = new createjs.LoadQueue(false);
	manifest=[
			{src:'/static/lottery/assets/background.png', id:'background'},
			{src:'/static/lottery/assets/logo.png', id:'logo'},
			{src:'/static/lottery/assets/button_start.png', id:'buttonStart'},
			
			{src:'/static/lottery/assets/item_ball.png', id:'itemBall'},
			{src:'/static/lottery/assets/item_ball_dim.png', id:'itemBallDim'},
			{src:'/static/lottery/assets/item_ball_guess.png', id:'itemBallGuess'},
			{src:'/static/lottery/assets/item_ball_bonus.png', id:'itemBallBonus'},
			{src:'/static/lottery/assets/item_ball_hit.png', id:'itemBallHit'},
			
			{src:'/static/lottery/assets/item_ball_bg.png', id:'itemBallBg'},
			{src:'/static/lottery/assets/item_ball_shadow.png', id:'itemBallShadow'},
			
			{src:'/static/lottery/assets/item_sphere.png', id:'itemSphere'},
			{src:'/static/lottery/assets/item_stick.png', id:'itemStick'},
			{src:'/static/lottery/assets/item_shine.png', id:'itemShine'},
			{src:'/static/lottery/assets/item_bar.png', id:'itemBar'},
			{src:'/static/lottery/assets/item_bar_bonus.png', id:'itemBarBonus'},
			
			{src:'/static/lottery/assets/item_card.png', id:'itemCard'},
			{src:'/static/lottery/assets/item_number_bg.png', id:'itemNumberBg'},
			{src:'/static/lottery/assets/item_number_select_bg.png', id:'itemNumberSelectBg'},
			{src:'/static/lottery/assets/button_lucky.png', id:'buttonLucky'},
			{src:'/static/lottery/assets/button_sphere.png', id:'buttonSphereStart'},
			{src:'/static/lottery/assets/item_table.png', id:'itemTable'},
			
			{src:'/static/lottery/assets/item_prize_bg.png', id:'itemPrizeBg'},
			{src:'/static/lottery/assets/item_prize_select_bg.png', id:'itemPrizeSelectBg'},
			
			{src:'/static/lottery/assets/button_confirm.png', id:'buttonConfirm'},
			{src:'/static/lottery/assets/button_cancel.png', id:'buttonCancel'},
			{src:'/static/lottery/assets/item_exit.png', id:'itemExit'},
			
			{src:'/static/lottery/assets/item_result.png', id:'itemResult'},
			{src:'/static/lottery/assets/button_continue.png', id:'buttonContinue'},
			{src:'/static/lottery/assets/button_facebook.png', id:'buttonFacebook'},
			{src:'/static/lottery/assets/button_twitter.png', id:'buttonTwitter'},
			{src:'/static/lottery/assets/button_whatsapp.png', id:'buttonWhatsapp'},
			{src:'/static/lottery/assets/button_fullscreen.png', id:'buttonFullscreen'},
			{src:'/static/lottery/assets/button_sound_on.png', id:'buttonSoundOn'},
			{src:'/static/lottery/assets/button_sound_off.png', id:'buttonSoundOff'},
			{src:'/static/lottery/assets/button_exit.png', id:'buttonExit'},
			{src:'/static/lottery/assets/button_settings.png', id:'buttonSettings'},
			
			{src:'/static/lottery/assets/button_left.png', id:'buttonLeft'},
			{src:'/static/lottery/assets/button_right.png', id:'buttonRight'}];
	
	soundOn = true;
	if($.browser.mobile || isTablet){
		if(!enableMobileSound){
			soundOn=false;
		}
	}
	
	if(soundOn){
		manifest.push({src:'/static/lottery/assets/sounds/click.ogg', id:'soundClick'});
		manifest.push({src:'/static/lottery/assets/sounds/balls.ogg', id:'soundBalls'});
		manifest.push({src:'/static/lottery/assets/sounds/reveal.ogg', id:'soundReveal'});
		manifest.push({src:'/static/lottery/assets/sounds/startspin.ogg', id:'soundStartSpin'});
		manifest.push({src:'/static/lottery/assets/sounds/win.ogg', id:'soundWin'});
		manifest.push({src:'/static/lottery/assets/sounds/suck.ogg', id:'soundSuck'});
		manifest.push({src:'/static/lottery/assets/sounds/complete.ogg', id:'soundComplete'});
		manifest.push({src:'/static/lottery/assets/sounds/number.ogg', id:'soundNumber'});
		manifest.push({src:'/static/lottery/assets/sounds/random.ogg', id:'soundRandom'});
		manifest.push({src:'/static/lottery/assets/sounds/cage.ogg', id:'soundCage'});
		manifest.push({src:'/static/lottery/assets/sounds/fail.ogg', id:'soundFail'});
		
		createjs.Sound.alternateExtensions = ["mp3"];
		loader.installPlugin(createjs.Sound);
	}
	
	loader.addEventListener("complete", handleComplete);
	loader.addEventListener("fileload", fileComplete);
	loader.addEventListener("error",handleFileError);
	loader.on("progress", handleProgress, this);
	loader.loadManifest(manifest);
}

/*!
 * 
 * CANVAS FILE COMPLETE EVENT - This is the function that runs to update when file loaded complete
 * 
 */
function fileComplete(evt) {
	var item = evt.item;
	//console.log("Event Callback file loaded ", evt.item.id);
}

/*!
 * 
 * CANVAS FILE HANDLE EVENT - This is the function that runs to handle file error
 * 
 */
function handleFileError(evt) {
	console.log("error ", evt);
}

/*!
 * 
 * CANVAS PRELOADER UPDATE - This is the function that runs to update preloder progress
 * 
 */
function handleProgress() {
	$('#mainLoader span').html(Math.round(loader.progress/1*100)+'%');
}

/*!
 * 
 * CANVAS PRELOADER COMPLETE - This is the function that runs when preloader is complete
 * 
 */
function handleComplete() {
	toggleLoader(false);
	initMain();
};

/*!
 * 
 * TOGGLE LOADER - This is the function that runs to display/hide loader
 * 
 */
function toggleLoader(con){
	if(con){
		$('#mainLoader').show();
	}else{
		$('#mainLoader').hide();
	}
}