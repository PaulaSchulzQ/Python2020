//1/ **Obtén del 1 al 255: Escribe una función que devuelve un array con todos los números del 1 al 255.
var z = [];

function array() {
    for (i = 1; i <= 250; i++) {
        z.push(i);
    }
    console.log(z);
}
console.log(array());

//2/ Consigue pares hasta 1000: Escribe una función que entregue la suma de todos los números pares del 1 al 1000 -
// Puedes usar un operador de módulo para este ejercicio. 
function SumPares() {
    sum = 0
    for (i = 0; i <= 1000; i += 2) {
        sum = sum + i;
    }
    return sum;
}
console.log(SumPares())

//3/ Suma impares hasta 5000: Escribe una función que devuelva la suma de 
//todos los números impares entre 1 y 5000 (ej: 1+3+5+...+4997+4999).
function SumImpares() {
    sum = 0
    for (i = 1; i <= 5000; i += 2) {
        sum = sum + i;
    }
    return sum
}
console.log(SumImpares())

//4/ Itera un array: Escribe una función que devuelva la suma de todos los valores dentro de un array 
//(ej:  [1,2,5] retorna 8. [-5,2,5,12] retorna 14). 

function SumArr(x) {
    if (x.length >= 1) {
        sum = 0;
        for (var i = 0; i < x.length; i++) {
            sum = sum + x[i];
        }
        return sum;
    }
    return x;
}

a = SumArr([1, 2, 3, 4, 5]);
console.log(a);


//5/ Encuentra el mayor (max): Dado un array con múltiples valores, 
//escribe una función que devuelva el número mayor (ej: para [-3,3,5,7] el número mayor (max) es 7). 
function MaxArr(x) {
    if (x.length > 1) {
        max = x[0];
        for (var i = 0; i < x.length; i++) {
            if (max <= x[i]) {
                max = x[i];
            }
        }
        return max;
    }
    return x;
}
a = MaxArr([-2, 3, 0, 4, 8, 2]);
console.log(a);


//6/ Encuentra el promedio (avg): Dado un array con múltiples valores, 
//escribe una función que devuelva el promedio de los valores (ej: para [1,3,5,7,20] el promedio es 7.2).
function PromArr(x) {
    sum = x[0];
    if (x.length >= 1) {
        for (var i = 1; i < x.length; i++) {
            sum = sum + x[i]
        }
        sum = sum / x.length;
        return sum;
    }
    return x;
}
a = PromArr([1, 3, 5, 7, 20]);
console.log(a);

//7/ Array de impares: Escribe una función que devuelva un array de 
// todos los números impares entre 1 y 50 (ej: [1,3,5, …, 47,49]). Pista: Usa el método ‘push’.
function Impares() {
    Impares = [];
    for (var i = 1; i < 50; i += 2) {
        Impares.push(i)
    }
    return Impares;
}
a = Impares()
console.log(a)

//8/ Mayor que Y: Dado un valor Y, escribe una función que toma un array y devuelve los valores mayores que Y. 
//Por ejemplo, si arr = [1,3,5,7] y Y = 3, tu función devolverá 2 (hay 2 números en el array mayores que 3, esto son 5 y 7). 
function Mayorque(x, y) {
    if (x.length >= 1 && y != undefined) {
        arr = [];
        for (var i = 0; i < x.length; i++) {
            if (x[i] > y) {
                arr.push(x[i]);
            }
        }
        return arr;
    }
    return "revisar"
}
a = Mayorque([1, 2, 3, 4, 5, 6, 7, 8, 9], 7);
console.log(a);

//9/ Cuadrados: Dado un array con múltiples valores, escribe una función que 
//reemplace cada valor por el cuadrado del mismo valor (ej: [1,5,10,-2] será [1,25,100,4]).
function valorcuadrado(x) {
    arr = [];
    for (var i = 0; i < x.length; i++) {
        arr[i] = x[i] * x[i];
    }
    return arr
}
a = valorcuadrado([1, 5, 10, -2]);
console.log(a);

//10/ Negativos: Dado un array con múltiples valores, escribe una función que reemplace 
//cualquier número negativo dentro del array por 0. Cuando el programa esté listo, 
//el array no debiera contener números negativos (ej: [1,5,10,-2] se convertirá en [1,5,10,0]).
function negcero(array) {
    for (let i = 0; i < array.length; i++) {
        if (array[i] < 0) {
            array[i] = 0;
        }
    }
    return array;
}
console.log(negcero([1, 5, 10, -2]));

//11/ Max/Min/Avg: Dado un array con múltiples valores, 
// escribe una función que devuelva un nuevo array que solo contenga el valor mayor (max), 
//menor (min) y promedio (avg) del array original (ej: [1,5,10,-2] devolverá [10,-2,3.5]).
function maxminavg(array) {
    max = array[0];
    min = array[0];
    avg = array[0];

    for (var i = 0; i < array.length; i++) {
        avg = avg + array[i];
        avg = avg / array.length;
        if (max < array[i]) {
            max = array[i];
            if (min > array[i]) {
                min = array[i];
            }
        }
        return [max, min, avg];
    }
}
console.log(maxminavg([1, 5, 10, -2]));

//12/ Intercambia Valores: Escribe una función que intercambie el primer y el último valor de cualquier array.
// La extensión mínima predeterminada del array es 2 (ej: [1,5,10,-2] será [-2,5,10,1]). 
function cambiaval(array) {
    ultimo = array[array.length - 1];
    array[array.length - 1] = array[0];
    array[0] = ultimo;
    return array;
}
console.log(cambiaval([1, 5, 10, -2]));

//13/ De Número a String: Escribe una función que tome un array de números y 
//reemplace cualquier valor negativo por el string ‘Dojo’. 
//Por ejemplo, dado el array = [-1,-3,2], tu función devolverá [‘Dojo’,‘Dojo’,2].

function numstring(array) {
    for (var i = 0; i < array.length; i++) {
        if (array[i] < 0) {
            array[i] = "Dojo";
        }
    }
    return array;
}
console.log(numstring([-1, -3, 2]));