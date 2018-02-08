# quesobabas 🧀
Lo mas grueso de la sabiduría alburera ha llegado a GitHub 🌶

- Telegram: [@quesobabasbot](https://telegram.me/quesobabasbot)
- Twitter: [@ilovequesobabas](https://twitter.com/ilovequesobabas)

### ¿Cómo funciona?

Inicialmente una instancia no entrenada de _quesobabas_ no sabe alburear. Cada
que un usuario lo alburea, guarda el albur recibido y la repuesta dada. Entre
más albures reciba, aumenta su repertorio y albureará con mayor precision.

Para responder un albur, _quesobabas_ buscará la respuesta del albur más parecido
en su repertorio de albures, esto basado en la frecuencia han sido utilizados en
otras conversaciones.

### Entrenamiento

En el directorio `data/` encontrarás un conjunto de datos que puede ser utilizado
para entrenar una instancia del quesobabas. Ejecuta el siguiente script para
entrenar tu propia instancia:

```sh
python quesobabas/train.py
```

Las contribuciones a este conjunto de datos son muy apreciadas. Si deseas agregar
mas albures, puedes hacer un pull request.

## Autores

* **Luis Alfredo Lorenzo** (A.K.A. [@babasbot](https://twitter.com/babasbot))

## Licencia

Este proyecto es software libre y es publicado bajo una [licencia MIT](LICENSE.txt).

