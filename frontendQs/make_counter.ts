
//  () => {}     arrow function, takes no arguments and returns something 
//  return a function that returns a number 
export default function makeCounter(initialValue: number = 0): () => number {
  let num = initialValue

  return () => {
    return num++
  }
}


// const counter = makeCounter();
// counter(); // 0
// counter(); // 1
// counter(); // 2