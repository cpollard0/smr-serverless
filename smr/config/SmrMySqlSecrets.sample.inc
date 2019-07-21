<?php
trait SmrMySqlSecrets {
	protected static $databaseName = 'smr_live';
	private static $host = '{{ mysql_host }}'; // must match MYSQL_HOST in .env
	private static $user = '{{ mysql_user }}';       // must match MYSQL_USER in .env
	private static $password = '{{ mysql_password }}';   // must match MYSQL_PASSWORD in .env

	// Set to null to use defaults
	private static $port = null;
	private static $socket = null;

	// Uncomment if using history databases
	//protected static $dbName_Smr12History = 'smr_12_history';
	//protected static $dbName_SmrClassicHistory = 'smr_classic_history';
}
