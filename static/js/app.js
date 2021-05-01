const counters= document.querySelectorAll('.counter');
const speed= 200;
counters.forEach(counter =>
  {
    const updateCount = () =>
  {
    const target= +counter.getAttribute('data-target');
    const count = +counter.innerText;
    //console.log(count);
    const inc= Math.ceil(target/speed);
    if(count<target)
    {
      counter.innerText = count + inc;
      setTimeout(updateCount,60);
    }
    else{
      counter.innerText = target;
    }
  }

 updateCount();
});

const but= document.getElementsByClassName("button")[0];
