function doClear(theText) { if (theText.value == theText.defaultValue) { theText.value = "" } }
function doDefault(theText) { if (theText.value == "") { theText.value = theText.defaultValue } }

 $(document).ready(function(){
	   $('.animate img').hover(
		function(){
			var $this = $(this);
				$this.stop().animate({'opacity':'0.7'});
			},
			function(){
				var $this = $(this);
					$this.stop().animate({'opacity':'1.0'});
				}
			);				
	});