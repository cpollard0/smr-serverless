<table class="standard">
	<tr>
		<th>Members</th>
		<th>Current</th>
		<th>Max</th>
	</tr>
	<tr>
		<td>Veteran</td>
		<td class="center"><?php echo $ThisAlliance->getNumVeterans(); ?></td>
		<td class="center"><?php echo $ThisGame->getAllianceMaxVets(); ?></td>
	</tr>
	<tr>
		<td>Total</td>
		<td class="center"><?php echo $ThisAlliance->getNumMembers(); ?></td>
		<td class="center"><?php echo $ThisGame->getAllianceMaxPlayers(); ?></td>
	</tr>
</table>

<br /><br />
<h2>Invite Player</h2>

<?php
if (count($InvitePlayers) == 0) { ?>
	<p>There are no players eligible to be invited to your alliance!</p><?php
} else { ?>

	<p>Select a player to invite to your alliance:</p>

	<form method="POST" action="<?php echo $InviteHREF; ?>">
		<select name="account_id" class="InputFields" size="1">
			<?php
			foreach ($InvitePlayers as $InvitePlayer) { ?>
				<option value="<?php echo $InvitePlayer->getAccountID(); ?>">
					<?php echo $InvitePlayer->getDisplayName(true); ?>
				</option><?php
			} ?>
		</select>
		<br />
		<p>Optional invitation message:</p>
		<textarea spellcheck="true" name="message" style="height: 5em"></textarea>
		<p>Days until invitation expires:</p>
		<input type="number" name="expire_days" value="7" />
		<br /><br />
		<input type="submit" name="action" class="InputFields" value="Invite Player" />
	</form><?php
} ?>

<br /><br />
<h2>Pending Invitations</h2>

<?php
if (count($PendingInvites) == 0) { ?>
	<p>Your alliance has no pending invitations.</p><?php
} else { ?>
	<br />
	<table class="standard">
		<tr>
			<th>Invited Player</th>
			<th>Invited By</th>
			<th>Expires</th>
		</tr><?php
		foreach ($PendingInvites as $invite) { ?>
			<tr>
				<td><?php echo $invite['invited']; ?></td>
				<td><?php echo $invite['invited_by']; ?></td>
				<td><?php echo $invite['expires']; ?></td>
			</tr><?php
		} ?>
	</table><?php
} ?>
