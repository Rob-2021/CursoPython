<?php
set_time_limit(300);

$archivo_csv = 'C:/xampp/htdocs/pandas/evaluaciones/users_new_ver.csv';
$nuevo_archivo_csv = 'C:/xampp/htdocs/pandas/evaluaciones/encriptado/data_users_new_ver_encriptado.csv';

// Abrir el archivo CSV original para lectura
if (($handle = fopen($archivo_csv, 'r')) !== FALSE) {
    $data = [];
    
    // Leer todas las filas del archivo CSV
    while (($row = fgetcsv($handle, 1000, ';')) !== FALSE) {
        // Encriptar la columna password (asumiendo que está en la posición 4)
        if (isset($row[4])) {
            $row[4] = password_hash($row[4], PASSWORD_BCRYPT);
        }
        $data[] = $row;
    }
    fclose($handle);
    
    // Abrir un nuevo archivo CSV para escritura
    if (($handle = fopen($nuevo_archivo_csv, 'w')) !== FALSE) {
        // Escribir todas las filas en el nuevo archivo CSV
        foreach ($data as $row) {
            fputcsv($handle, $row, ';');
        }
        fclose($handle);
    }
    
    echo "Las contraseñas han sido encriptadas y guardadas en $nuevo_archivo_csv";
} else {
    echo "No se pudo abrir el archivo $archivo_csv";
}
?>
