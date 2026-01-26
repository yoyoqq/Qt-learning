// export default -> this file exports only exports its function, can import without curly braces
export default function mean(array: number[]): number {
    let ans = 0;
    for (let i=0; i<array.length; i++){
        ans += array[i];
    }
    return ans / array.length;
}