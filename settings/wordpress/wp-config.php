<?php
/**
 * The base configuration for WordPress
 *
 * The wp-config.php creation script uses this file during the
 * installation. You don't have to use the web site, you can
 * copy this file to "wp-config.php" and fill in the values.
 *
 * This file contains the following configurations:
 *
 * * MySQL settings
 * * Secret keys
 * * Database table prefix
 * * ABSPATH
 *
 * @link https://wordpress.org/support/article/editing-wp-config-php/
 *
 * @package WordPress
 */

// ** MySQL settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define( 'DB_NAME', 'secretdb' );

/** MySQL database username */
define( 'DB_USER', 'secretuser' );

/** MySQL database password */
define( 'DB_PASSWORD', '9b2f70fe6ebb88c0ae0f2a2f4ca66c42' );

/** MySQL hostname */
define( 'DB_HOST', 'localhost' );

/** Database Charset to use in creating database tables. */
define( 'DB_CHARSET', 'utf8' );

/** The Database Collate type. Don't change this if in doubt. */
define( 'DB_COLLATE', '' );

/**#@+
 * Authentication Unique Keys and Salts.
 *
 * Change these to different unique phrases!
 * You can generate these using the {@link https://api.wordpress.org/secret-key/1.1/salt/ WordPress.org secret-key service}
 * You can change these at any point in time to invalidate all existing cookies. This will force all users to have to log in again.
 *
 * @since 2.6.0
 */
define('AUTH_KEY',         'kzglvO;k$F_-W68 Fl*iEekX;-pn =fNS(;c6nDKt;5RW(&jtESBsW9+PhQFS!Tv');
define('SECURE_AUTH_KEY',  ',,F|NHKh>=+y.gy%B32Ff!s~MJp$L,]~xEK|e3H)7| 4hX]!/Ky@V(esZa?0D#H*');
define('LOGGED_IN_KEY',    'k7o7@~oee{u,MG KFBJq0M`-iJ0H0hs)m-@i/RsgwZ{No~JQ+)2A<Ryd+|t<8.[a');
define('NONCE_KEY',        'f54j6Auj0NT8g;5-^zk}yZ`vN^8/7!6=%5bS>GUu{04~#E*a~WdGX<%>Aa<Ke}K8');
define('AUTH_SALT',        '?PULIL7?y%Ub=[~rw+5Pg^!$UrrOpn*Pr(MFBdF-+ZMH#oKsZ{KskZY9m/i|<pkK');
define('SECURE_AUTH_SALT', 'of~0;WuAmEBP4~rfM)1Q.Oc0U=g^t|d%h.Ui8w<v4;A47FGs0}@Hk>&g?p*hDoQs');
define('LOGGED_IN_SALT',   'WTc*{p+XT((_#^NxhoU)[7NAg};Q?`+0wpkia>oA]hF-TB2lC GM!~aM=-Hqw4,+');
define('NONCE_SALT',       '^[_9^w_,UPMuJ2-}7=y<|v=y$#xftY[klEW3zt,Y}bB tG4d):p9Fd;$imF[lGqR');

/**#@-*/

/**
 * WordPress Database Table prefix.
 *
 * You can have multiple installations in one database if you give each
 * a unique prefix. Only numbers, letters, and underscores please!
 */
$table_prefix = 'wp_';

/**
 * For developers: WordPress debugging mode.
 *
 * Change this to true to enable the display of notices during development.
 * It is strongly recommended that plugin and theme developers use WP_DEBUG
 * in their development environments.
 *
 * For information on other constants that can be used for debugging,
 * visit the documentation.
 *
 * @link https://wordpress.org/support/article/debugging-in-wordpress/
 */
define( 'WP_DEBUG', false );

/* That's all, stop editing! Happy publishing. */

/** Absolute path to the WordPress directory. */
if ( ! defined( 'ABSPATH' ) ) {
	define( 'ABSPATH', __DIR__ . '/' );
}

/** Sets up WordPress vars and included files. */
require_once ABSPATH . 'wp-settings.php';
