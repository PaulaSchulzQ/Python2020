//**1/ Tamaño Grande - Dado un array, escribe una función que cambie todos los números positivos en él,
// por el string “big”. Ejemplo: grande([-1,3,5,-5]) devuelve [-1, “big”, “big”, -5].
function stringbig(array) {
    for (var i = 0; i < array.length; i++) {
        if (array[i] > 0) {
            array[i] = "big";
        }
    }
    return array;
}
a = stringbig([-1, 3, 5, -5]);
console.log(stringbig(a));

//2/ Imprime (print) el menor, devuelve (return) el mayor - 
//Crea una función que tome un array de números. 
//La función debería imprimir (print) el menor valor del array, y devolver (return) el mayor. 
function printreturn(array) {
    menor = array[0];
    mayor = array[0];
    for (var i = 0; i < array.length; i++) {
        if (menor >= array[i]) {
            menor = array[i];
        }
        if (mayor <= array[i]) {
            mayor = array[i];
        }
    }
    console.log(menor);
    return mayor;
}
a = printreturn([1, 2, 3, 4, 5]);

//3/ Imprime (print) uno, devuelve (return) otro- 
//Crea una función para un array de números.
// La función debería imprimir (print) el penúltimo valor y devolver (return) el primer valor impar.
function printreturnot(array) {
    impar = [];
    for (var i = 0; i < array.length; i++) {
        if ((array[i]) % 2 != 0) {
            impar.push(array[i]);
        }
    }
    console.log(array[array.length - 2]);
    return impar[0];
}
a = printreturnot([2, 3, 5, 7, 6, 7, 8, 0]);


//4/ Doble Visión - 
//Dado un array, crea una función que devuelva un nuevo array donde cada valor se duplique. 
//Entonces, doble([1,2,3]) debiera devolver [2, 4, 6] sin cambiar el array original. 
function duplica(array) {
    nuevoarr = [];
    for (var i = 0; i < array.length; i++) {
        nuevoarr.push(array[i] * 2);
    }
    return nuevoarr;
}
a = duplica([1, 2, 3]);

//5/ Contar Positivos - 
// Dado un array de números, crea una función para reemplazar 
//el último valor con el número de valores positivos encontrados en el array.
// Ejemplo, contarPositivos([-1,1,1,1]) cambia el array original y devuelve [-1,1,1,3].
function contarpositivos(array) {
    cuantos = [];
    for (var i = 0; i < array.length; i++) {
        if (array[i] > 0) {
            cuantos.push(array[i]);
        }
    }
    array[array.length - 1] = cuantos.length;
    return array;
}
a = contarpositivos([-1, 1, 1, 1]);


//6/ Pares e Impares - 
//Crea una función que acepte un array. 
//Cada vez que ese array tenga 3 valores impares seguidos, 
//imprime (print) “¡Qué imparcial!”, y cada vez que tenga 3 pares seguidos, imprime (print) “¡Es para bien!”.
function parimpar(array) {
    for (var i = 0; i < array.length; i++) {
        if (array[i] % 2 == 0 && array[i + 1] % 2 == 0 && array[i + 2] % 2 == 0) {
            console.log("es para bien");
        } else if (array[i] % 2 != 0 && array[i + 1] % 2 != 0 && array[i + 2] % 2 != 0) {
            console.log("que imparcial");
        }

    }
}
a = parimpar([3, 1, 5, 2, 4, 8, 1, 6, 8, 4]);

//7/ Incrementa los Segundos - 
// Dado un array de números arr, 
//agrega 1 a cualquier otro elemento, específicamente a aquellos cuyo 
//índice es impar (arr[1], arr[3], arr[5], etc). 
//Luego, console.log cada valor del array y devuelve arr. 
function agregauno(array) {
    for (var i = 0; i < array.length; i++) {
        if (i % 2 != 0) {
            array[i] = array[i] + 1;
        }
        console.log(array[i]);
    }
    return array;
}
a = agregauno([0, 1, 2, 3, 4, 5, 6, 7])

//8/ Longitudes previas - 
// Pasado un array (similar a decir ‘tomado un array’ o ‘dado un array’)
// que contiene strings, reemplaza cada string con un número de acuerdo cantidad de letras (longitud) del string anterior. 
//Por ejemplo, longitudesPrevias([“programar”,“dojo”, “genial”]) debería devolver [“programar”,9, 4]. 
//Pista: ¿For loops solo puede ir hacia adelante?
function stringsnum(array) {
    nuevoarray = [];
    cantidadletras = [];
    for (var i = 0; i < array.length; i++) {
        cantidadletras.push(array[i].length);
        nuevoarray.push(array[i]);
    }
    for (var i = array.length - 1; i >= 1; i--) {
        nuevoarray[i] = cantidadletras[i - 1];
    }
    return nuevoarray;
}
a = stringsnum(["programar", "dojo", "genial"]);

//9/ Agrega Siete - 
//Construye una función que acepte un array. 
// Devuelve un nuevo array con todos los valores del original, pero sumando 7 a cada uno. 
// No alteres el array original. Por ejemplo, agregaSiete([1,2,3) debería devolver [8,9,10] en un nuevo array. 
function massiete(array) {
    nuevomas = [];
    for (var i = 0; i < array.length; i++) {
        nuevomas.push(array[i] + 7);
    }
    return nuevomas;
}
a = massiete([1, 2, 3]);


//10/ Array Inverso - 
// Dado un array, escribe una función que invierte sus valores en el lugar.
// Ejemplo: invertir([3,1,6,4,2)) devuelve el mismo array pero con sus valores al revés, es decir [2,4,6,1,3]. 
//Haz esto sin crear un array temporal vacío. (Pista: necesitarás intercambiar (swap) valores).
function invierte(array) {
    //[array[0], array[array.length - 1]] = [array[array.length - 1], array[0]];
    //esto sirve para cambiar elementos fijos (como el ultimo por el primero sin crear un temporal)
    //el .reverse sirve para invertir uno array completo o algunos elementos indicados. 
    array.reverse(array);
    return array;
}
a = invierte([3, 1, 6, 4, 2]);

//11/ Perspectiva: Negativa - 
//Dado un array crear y devuelve uno nuevo que contenga todos los valores del array original,
// pero negativos (no simplemente multiplicando por -1). Dado [1,-3,5], devuelve [-1,-3,-5].
function negativos(array) {
    todosnegativos = [];
    for (var i = 0; i < array.length; i++) {
        if (array[i] < 0) {
            todosnegativos.push(array[i]);
        } else if (array[i] > 0) {
            array[i] = (array[i]) * -1;
            todosnegativos.push(array[i]);
        }
    }
    return todosnegativos;
}
a = negativos([1, -3, 5]);

//12/ Siempre hambriento - 
//Crea una función que acepte un array e imprima (print) “yummy” cada vez que alguno de los valores sea “comida”.
// Si ningún valor es “comida”, entonces imprime “tengo hambre” una vez. 
function hambriento(array) {
    tengohambre = [];
    for (i = 0; i < array.length; i++) {
        if (array[i] == "comida") {
            console.log("yummy");
        }
    }
    if (array.includes("comida")) {} else {
        console.log("tengo hambre")
    }
}

a = hambriento(["comida", "hola", "comi"]);



//13// Cambiar hacia el centro -  
//Dado un array, cambia el primer y último valor, el tercero con el ante penútimo, etc. 
// Ejemplo: cambiaHaciaElCentro([true, 42, “Ada”, 2, “pizza”]) cambia el array a [“pizza¨, 42, “Ada”, true]. 
//cambiaHaciaElCentro([1,2,3,4,5,6]) cambia el array a [6,2,4,3,5,1]. No es necesario devolver (return) el array esta vez. 
function haciaelcentro(array) {
    for (i = 0; i <= array.length / 2; i += 2) {
        [array[i], array[array.length - 1 - i]] = [array[array.length - 1 - i], array[i]];
    }
    return array;
}
a = haciaelcentro([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]);

//14// Escala el Array - Dado un array arr y un número num, 
// multiplica todos los valores en el array arr por el número num, y devuelve el array arr modificado. 
// Por ejemplo, escalaArray([1,2,3], 3] debería devolver [3,6,9]. */
function escalaarr(x, y) {
    for (i = 0; i < x.length; i++) {
        x[i] = x[i] * y;
    }
    return x;
}
a = escalaarr([1, 2, 3], 3);