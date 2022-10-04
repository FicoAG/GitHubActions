Ejemplo
====

Esto es una prueba

.. code-block:: python
    get_numerical_features(df)
    return list(df.select_dtypes(include=[np.number]).columns)