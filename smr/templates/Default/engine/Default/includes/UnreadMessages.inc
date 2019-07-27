<span id="message_area"><?php
	if (isset($MessageGlobalLink)) { ?>
		<a href="<?php echo $MessageGlobalLink; ?>"><img src="<?php echo STATIC_ASSETS;?>/images/global_msg.png" width="32" height="32" alt="Global Messages" /></a>
		<span class="small"><?php echo $MessageGlobalNum; ?></span><?php
	}
	if (isset($MessagePersonalLink)) { ?>
		<a href="<?php echo $MessagePersonalLink; ?>"><img src="<?php echo STATIC_ASSETS;?>/images/personal_msg.png" width="32" height="32" alt="Personal Messages" /></a>
		<span class="small"><?php echo $MessagePersonalNum; ?></span><?php
	}
	if (isset($MessageScoutLink)) { ?>
		<a href="<?php echo $MessageScoutLink; ?>"><img src="<?php echo STATIC_ASSETS;?>/images/scout_msg.png" width="32" height="32" alt="Scout Messages" /></a>
		<span class="small"><?php echo $MessageScoutNum; ?></span><?php
	}
	if (isset($MessagePoliticalLink)) { ?>
		<a href="<?php echo $MessagePoliticalLink; ?>"><img src="<?php echo STATIC_ASSETS;?>/images/council_msg.png" width="32" height="32" alt="Political Messages" /></a>
		<span class="small"><?php echo $MessagePoliticalNum; ?></span><?php
	}
	if (isset($MessageAllianceLink)) { ?>
		<a href="<?php echo $MessageAllianceLink; ?>"><img src="<?php echo STATIC_ASSETS;?>/images/alliance_msg.png" width="32" height="32" alt="Alliance Messages" /></a>
		<span class="small"><?php echo $MessageAllianceNum; ?></span><?php
	}
	if (isset($MessageAdminLink)) { ?>
		<a href="<?php echo $MessageAdminLink; ?>"><img src="<?php echo STATIC_ASSETS;?>/images/admin_msg.png" width="32" height="32" alt="Admin Messages" /></a>
		<span class="small"><?php echo $MessageAdminNum; ?></span><?php
	}
	if (isset($MessageCasinoLink)) { ?>
		<a href="<?php echo $MessageCasinoLink; ?>"><img src="<?php echo STATIC_ASSETS;?>/images/casino_msg.png" width="32" height="32" alt="Casino Messages" /></a>
		<span class="small"><?php echo $MessageCasinoNum; ?></span><?php
	}
	if (isset($MessagePlanetLink)) { ?>
		<a href="<?php echo $MessagePlanetLink ?>"><img src="<?php echo STATIC_ASSETS;?>/images/planet_msg.png" width="32" height="32" alt="Planet Messages" /></a>
		<span class="small"><?php echo $MessagePlanetNum; ?></span><?php
	}
	if (isset($MessageGlobalLink) || isset($MessagePersonalLink) || isset($MessageScoutLink) || isset($MessagePoliticalLink) || isset($MessageAllianceLink) || isset($MessageAdminLink) || isset($MessageCasinoLink) || isset($MessagePlanetLink)) {
		?><br /><?php
	} ?>
</span>
