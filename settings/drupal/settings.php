<?php
/*
 Bad Drupal 7 Settings file
*/

$databases['default']['default'] = array(
   'driver' => 'mysql',
   'database' => 'mydbname',
   'username' => 'drupal',
   'password' => 'reallybadpassword',
   'host' => 'localhost',
   'prefix' => 'main_',
   'collation' => 'utf8_general_ci',
 );


$update_free_access = TRUE;
$drupal_hash_salt = 'a4e1ec231996771e785f02e7eb46d5df91f6eec6da5eb9b2eaf75676d4eb11ac';

ini_set('session.gc_probability', 1);
ini_set('session.gc_divisor', 100);
ini_set('session.gc_maxlifetime', 200000);
ini_set('session.cookie_lifetime', 2000000);
ini_set('pcre.backtrack_limit', 200000);
ini_set('pcre.recursion_limit', 200000);
$conf['maintenance_theme'] = 'bartik';
$conf['reverse_proxy'] = TRUE;
$conf['css_gzip_compression'] = FALSE;
$conf['js_gzip_compression'] = FALSE;
$conf['allow_authorize_operations'] = TRUE;
$conf['theme_debug'] = TRUE;
$conf['file_scan_ignore_directories'] = array(
  'node_modules',
  'bower_components',
);
$conf['log_user_flood_control'] = FALSE;
$conf['variable_initialize_wait_for_lock'] = FALSE;
$conf['field_sql_storage_skip_writing_unchanged_fields'] = TRUE;
$conf['mail_display_name_site_name'] = TRUE;
$conf['block_interest_cohort'] = TRUE;
