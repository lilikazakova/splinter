<script src="//ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min.js"></script>

<p id="1"style="border: 5px solid"> Initial Text 1</p>
<p id="2"style="border: 5px solid"> Initial Text 2</p>
<p id="3"style="border: 5px solid"> Initial Text 3</p>
<input id="b1" type="button" value="Hide 1">
<input id="b2" type="button" value="Hide 2">
<input id="b3" type="button" value="Hide 3">

<script>
function hue()  {
    return 'rgb('
        	+ (Math.floor(Math.random() * 256)) + ','
            + (Math.floor(Math.random() * 256)) + ','
            + (Math.floor(Math.random() * 256)) + ')';
}
    
 
$("#1").css("border-color",hue() );
$("#2").css("border-color",hue() );
$("#3").css("border-color",hue() );

/* function change_text(x) {
    return $(this).text("'Changed text'+x");  
}

$("#1").hover( change_text() );    */

$("#1").hover(function(){
   	$("#1").text("Changed text 1");
});
      
$("#2").click(function(){
   	$("#2").text("Changed text 2");
});
        
$("#3").dblclick(function(){
   	$("#3").text("Changed text 3");
});

$("#1").mouseleave(function(){
   	$("#1").text("Initial text 1");
});
    
$("#2").mouseleave(function(){
   	$("#2").text("Initial text 2");
});
        
$("#3").mouseleave(function(){
   	$("#3").text("Initial text 3");
});

function btn_change(button, p) {
var clicks = true;
    $(button).click(function() {
        if (clicks) {
            $(button).val("Show 1");
            $(p).hide();
            
            clicks = false;
        } else {
                $(p).show();
                $(button).val("Hide 1");
                clicks = true;
          }  
    });
}

$("#b1").click(btn_change( $("#b1"), $("#1") ) );
$("#b2").click(btn_change( $("#b2"), $("#2") ) );
$("#b3").click(btn_change( $("#b3"), $("#3") ) );

</script>
