function expand( id ) { 
  var box = document.getElementById( id );
  if( box.style.display=="none" ) { 
    box.style.display="block";
  } else {
    box.style.display="none";
  }
}
