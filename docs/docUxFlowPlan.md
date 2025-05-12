## Landing Page:
- Obj: inform user of what this is, and get them to sign up

## Login/Register Page:
- Remember, the login has email verification

## User Home Page
- Create world (goto world creation page)
- Join world (with join code. goto world page)
- View all worlds created by the user or joined
- "Hot Load" most recent campaign (goto campaign page)
- View calendar (google calendar integration?) showing world/campaign event/session days for the user
- View recent events log (aggregate from all campaigns or worlds) in order sent out
- View other notifications
- User profile/settings
- Potential access to other features (marketplace)

## Create World Page
### 1. User uploads map
- Display standardized grid over map
- Right clicking square in grid subdivides square into 4 smaller ones, allowing for more precise selections. Shift + right click combines back to normal size.

### 2. Region Creation and Selection (for fog of war)
- User can skip this process (so no "fog of war")
- Show column of "regions"
- User can create new region and add name + color. User can also delete region made.
- Once at least one region has been made and selected, user can begin selecting squares in the grid to denote the map location of the region.
- Users can deselect a region square on the grid. Region squares do not have to be adjacent.
- After entire region has been selected, user can create another region and repeat the process until satisfied.

### 3. World Settings
- Set world name, description/lore, cover image, privacy (?)
- World privacy
    - Set visibility to public
    - Set joining methods: users can request to join, or do they require a direct invite?
- World permissions
    - Can DM's invite/accept players to join the world?
    - Campaign creation restrictions:
        - Can users create new campaigns?
        - Set max number of active campaigns
        - Set max numb
    - Can users from one campaign enter the campaign page for another one?
- Other settings
    - Set max users limit
    - Set category of notifications are sent out
    - Set spectator visibility of map: fog of war enabled for spectators?
    - Set shared inter-party visibility of regions (regions visible to players if another party has been there but they themselves have not)
    - Set party position viewing settings (Show current party positions even if user's party is "behind" in time)
    - Others??

### 4. Display World Page

## World Page
- Show world map as background
- Ability to pan (zoom maybe isn't required here)
- CLOUDS ANIMATED OVER MAP (perhaps png of cloud + shadow underneath laid flat with opacity 50% or something so it overlays on map without blocking view)
- (cool feature to add past MVP?) light mode has sun ray/lighting animations, dark mode shows night version of map?
- Depending on user role in the world (DM, Spectator, player) and world settings, the user can see the entire world (no fog of war blocking view)
- Regions discovered by the different parties are visible even if the user's party hasn't discovered it
- View names of ongoing campaigns in the world, as well as their players and DM's (user profiles)
- View current location of parties from all campaigns on map. Toggleable party path trails (from all parties)
- View notifications from the world
- View world's current age/date!!!
- View world lore/description
- If user has permissions (only editable in world settings, set by world creator), user can create campaign (goto campaign creation page)
- User can select their specific campaign (goto campaign page)

## Campaign Creation Page
- Set start location
- Set campaign banner
- Set campaign description/lore
- Set category of notifications are sent out (event, session creation, player joined/left, ?)
- Set session creation permissions:
    - Can players add to session info?
    - Can players modify their player stats change section in the session info?
- Option to send invites to players right away (can also do this later)

## Campaign Page
- Zoom in slightly on party's region upon campaign click
- Show party's current location
- Ability to zoom in/out in map
- Ability to pan around map
- Ability to center on party current location (or the location of the party at a certain session if slider used)
- Show slider: moving left shows party locations in previous sessions. Sliding right goes forwards in time until current session
- Show session list, displaying relevant session information
- Upon click of session (or session "scrolled" to via slider), open side panel showing more detailed session information:
    - Summary of what happened in the session
    - Images or other fields edited by the DM or Spectator (if given permission, only editable in campaign settings, set by campaign creator)
    - (maybe add past MVP: Elden Ring stats page showing changes in all player character's inventories/statuses. Eg. change in level, loss of health, items gained, etc. Just nets)
- Invite players to campaign (if allowed by world settings)
- If DM, user can create new session (goto session creation page/panel)
- If DM, user can edit past session info (even the title, start, and end location)

## Session Creation Panel/Page
- Idea is that the dm adds the session to their campaign after they have played it out IRL
- Set session title (required)
- Set session start location (required)
- Set session end location (required)
- Set world age when session ended (required)!!!
- Set session description
- Set session player changes
- Set player net stats/inventory changes


## > [!NOTE]
> What to do with world age/date? Way to automatically change date with advancing campaigns?
