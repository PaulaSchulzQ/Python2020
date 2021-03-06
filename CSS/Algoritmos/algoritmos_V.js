//**1 */

/*Configura un array para que los valores negativos se transformen en 0. 
Por ejemplo, resetNegativos([1,2,-1,-3]) debiera dar como resultado [1,2,0,0].*/

function resetNegativos(arreglo) {

    for (var i = 0; i < arreglo.length; i++) { // el indice o posición i=0
        if (arreglo[i] < 0) {
            arreglo[i] = arreglo[i] + (arreglo[i] * -1);
        }
    }
    return arreglo;
}

var resultado = resetNegativos([1, 2, -1, -3]);
console.log(resultado);
[1, 2, 0, 0]

/** 2*/
//.- Dado un array, mueve todos los valores un espacio de derecha a izquierda 
//eliminando el primer valor 
//y dejando un 0 para el último valor. 
//Por ejemplo, moverAdelante([1,2,3]) debiera dar como resultado [2,3,0].


function moverAdelante(arreglo) { //arreglo.length =  3 ; arreglo[arreglo.length-1] = 0
    let nuevoArreglo = []; //[]
    for (let i = 1; i < arreglo.length; i++) { //i=1
        //nuevoArreglo[i-1]=arreglo[i];
        nuevoArreglo.push(arreglo[i])
    }
    nuevoArreglo.push(0); //[2,3,0]
    return nuevoArreglo;
}


/**3 */
/*Configura un array para que el resultado sean los valores en el orden contrario. 
Por ejemplo, returnReverso([1,2,3,4]) debe dar [4,3,2,1].*/

function returnReverso(array) { //array= [1,2,3,4]; array.length = 4; 

    let nuevoArreglo = []; //[4,3,2,1]
    for (let i = array.length - 1; i >= 0; i--) { //i =3>2>1>0>-1
        nuevoArreglo.push(array[i]);
    }
    return nuevoArreglo;
}

console.log(returnReverso([1, 2, 3, 4])); //[4,3,2,1]

//**4 */
/*Crea una función que cambie un array repitiendo sus valores originales (manteniendo el mismo orden). 
Por ejemplo, repetirValores([4,”Ulysses”, 42, false]) 
debiera dar [4,4, “Ulysses”, “Ulysses”, 42, 42, false, false].*/

function repetirValores(array) {

    for (var i = array.length - 1; i >= 0; i--) {
        array[2 * (i + 1)] = array[i];
        array[2 * i] = array[i];
    }
    return array;
}

var resultado = repetirValores([4, "Ulysses", 42, false]);