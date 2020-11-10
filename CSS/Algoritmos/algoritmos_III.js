//**1 */
function a(x, y) { //x=5 y=5
    return 5;
}
console.log(a(5, 5))

//Resp: 5

//**2 */
function a(x, y) { //x=2 y=2 => x=6 y=8
    z = []
        //[2,2,5]   // [6,8,5]
    z.push(x);
    z.push(y);
    z.push(5);
    console.log(z); //[2,2,5]   // [6,8,5]
    return z;
}
b = a(2, 2) //b= [2,2,5]
console.log(b); //[2,2,5]
console.log(a(6, 8)); //[6,8,5]
//Resp: [2,2,5], [2,2,5], [6,8,5], [6,8,5]

//**3 */
function a(x) { //x=2
    z = [];
    //[2,2]
    z.push(x);
    z.pop();
    z.push(x);
    z.push(x);
    return z;
}
y = a(2); //y=[2,2]
y.push(5); //y=[2,2,5]
console.log(y);
//Resp: [2,2,5]

//**4 */
function a(x) {
    if (x[0] < x[1]) {
        return true;
    } else {
        return false;
    }
}
b = a([2, 3, 4, 5])
console.log(b);
//Resp: true, 

//**5 */
function a(x) {
    for (var i = 0; i < x.length; i++) {
        if (x[i] > 0) {
            x[i] = “Coding”;
        }    
    }
    //x=["coding", "coding", "coding", "coding"]
        
    return x;
}
console.log(a([1, 2, 3, 4]))
    //Resp: ["coding", "coding", "coding", "coding"]

//**6 */
function a(x) {
    for (var i = 0; i < x.length; i++) {
        if (x[i] > 5) {
            x[i] = “Coding”;
        } else if (x[i] < 0) {
            x[i] = “Dojo”;
        }    
    }    
    return x;
}
console.log(a([5, 7, -1, 4]))
    //Resp: [5, "coding", "dojo", 4]


//**7 */
function a(x) {
    if (x[0] > x[1]) {
        return x[1];
    }
    return 10;
}
b = a([5, 10]) // b=10
console.log(b);
//Resp: 10

//**8 */
function sum(x) {
    sum = 0;
    for (var i = 0; i < x.length; i++) {
        sum = sum + x[i];
        console.log(sum);
    }
    return sum;
}
//Resp: Undefined

///Segunda parte//

//**1 */
function printAverage(x) {
    sum = 0; //acumulador
    for (var i = 0; i < x.length; i++) {
        sum = sum + x[i];
    } //suma de todos / por la cantidad
    //var promedio = sum/x.length;
    return sum / x.length; //promedio
}
y = printAverage([1, 2, 3]);
console.log(y); // should log 2

y = printAverage([2, 5, 8]);
console.log(y); // should log 5

//**2 */
function returnOddArray() {
    var arreglo = []; //[1,3,5,7...,253,255]

    for (var i = 1; i <= 255; i += 2) { //i=1>3>...255>257
        arreglo.push(i);
    }
    //console.log(arreglo);//[1,3,5,7...,253,255]
    return arreglo

}
y = returnOddArray();
console.log(y); // should log [1,3,5,...,253,255]
//undefined



//**3 */
function squareValue(x) { //x= [1, 2, 3]; x.length=3

    for (var i = 0; i < x.length; i++) { //i=0>1>2>3
        //x[i] = -> si existre lo reemplaza
        x[i] = x[i] * x[i]; //x[2] = 3*3
    }
    return x; //[1,4,9]
}

y = squareValue([1, 2, 3]);
console.log(y); // should log [1,4,9]

y = squareValue([2, 5, 8]);
console.log(y); // should log [4,25,64]