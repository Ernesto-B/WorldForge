import { Header } from "../components/Header";
import background from "../assets/images/dnd-wallpaper-1.jpg";
import elf from "../assets/images/elf.png";
import background2 from "../assets/images/bg2.png";
import background3 from "../assets/images/bg1.jpg";
import {
  Box,
  Button,
  Card,
  CardContent,
  Stack,
  Typography,
} from "@mui/material";

export const HomePage = () => {
  return (
    <div className="min-h-fit bg-[#1b1b1b]">
      <Header />
      <main className="flex flex-col gap-40 px-10">
        <section className="relative overflow-hidden">
          <div className="relative w-full">
            <img
              src={background}
              alt="hero-background"
              className="brightness-[60%] rounded-2xl rounded-bl-[200px] w-full h-[1000px] object-cover"
            ></img>
            <svg
              className="absolute bottom-0 left-0 w-full"
              viewBox="0 0 1440 320"
              preserveAspectRatio="none"
            >
              <path
                fill="#1b1b1b"
                fill-opacity="1"
                d="M0,192L80,186.7C160,181,320,171,480,154.7C640,139,800,117,960,117.3C1120,117,1280,139,1360,149.3L1440,160L1440,320L1360,320C1280,320,1120,320,960,320C800,320,640,320,480,320C320,320,160,320,80,320L0,320Z"
              ></path>
            </svg>
          </div>
          <div className="absolute right-0 top-60 w-[900px] h-auto pointer-events-none">
            <img src={elf} alt="elf" className="w-full h-auto object-contain" />
            <div className="absolute inset-0 bg-gradient-to-b from-transparent to-[#1b1b1b] to-[90%]"></div>
          </div>
          <p className="absolute top-[500px] left-[100px] text-white font-serif text-6xl w-1/2">
            Because even the <span className="text-orange-500">mightiest</span>{" "}
            heroes forget where they left the{" "}
            <span className="text-orange-500">map</span>.
          </p>
        </section>
        <section className="bg-[#1b1b1b] flex gap-8">
          <img
            src={background2}
            className="w-1/2 h-[500px] shadow-black shadow-2xl rounded"
          />
          <div className="w-1/2 h-[500px] flex flex-col gap-4">
            <Typography
              variant="overline"
              fontSize="16px"
              color="white"
              fontWeight="bold"
            >
              What is WorldForge
            </Typography>
            <Typography variant="h2" fontSize="36px" color="white">
              A Living Atlas for Your D&D Campaigns
            </Typography>
            <Typography variant="body1" color="white" fontSize={20}>
              WorldForge transforms your campaign world into a dynamic,
              interactive map where every location tells a story. Whether you're
              a Dungeon Master managing lore or a player retracing epic quests,
              the map acts as the central hub for everything in your world —
              characters, session logs, locations, factions, and more.
            </Typography>
            <Typography variant="body1" color="white" fontSize={20}>
              Instead of scattered notes and fading memories, you get a
              visually-driven, persistent world that evolves with each session.
              Reveal new regions as players explore, track party movements, and
              log important events in a space everyone can revisit.
            </Typography>
            <Button
              variant="contained"
              sx={{
                bgcolor: "var(--color-orange-500)",
                fontWeight: "bold",
                fontSize: "16px",
                width: "fit-content",
                padding: "10px",
                marginTop: "20px",
                transition: "all 0.3s ease",
                "&:hover": {
                  bgcolor: "var(--color-orange-700)",
                },
              }}
            >
              Explore a Demo World
            </Button>
          </div>
        </section>
        <section className="bg-[#1b1b1b] flex gap-8">
          <div className="w-1/2 h-[500px] flex flex-col gap-4">
            <Typography
              variant="overline"
              fontSize="16px"
              color="white"
              fontWeight="bold"
            >
              Multi-Campaign, Shared World Support
            </Typography>
            <Typography variant="h2" fontSize="36px" color="white">
              Multiple Campaigns. One Living World
            </Typography>
            <Typography variant="body1" color="white" fontSize={20}>
              WorldForge lets you run multiple campaigns inside a single
              persistent world — perfect for long-term storytelling or
              collaborative universes. Whether you're juggling several parties
              or co-DMing with friends, each campaign has scoped visibility
              while still existing within the same evolving world.
            </Typography>
            <Typography variant="body1" color="white" fontSize={20}>
              You can track progress per group, synchronize global events, and
              even let players indirectly affect each other's stories through
              shared discoveries and outcomes.
            </Typography>
            <Button
              variant="contained"
              sx={{
                bgcolor: "var(--color-orange-500)",
                fontWeight: "bold",
                fontSize: "16px",
                width: "fit-content",
                padding: "10px",
                marginTop: "20px",
                transition: "all 0.3s ease",
                "&:hover": {
                  bgcolor: "var(--color-orange-700)",
                },
              }}
            >
              See How Campaign Sync Works
            </Button>
          </div>
          <img
            src={background3}
            className="w-1/2 h-[500px] shadow-black shadow-2xl object-cover rounded"
          />
        </section>
        <section>
          <Box
            sx={{
              position: "relative",
              overflow: "hidden",
              width: "100%",
              py: 4,
            }}
          >
            {/* Gradient Overlays */}
            <Box
              sx={{
                position: "absolute",
                top: 0,
                left: 0,
                width: "100px",
                height: "100%",
                background: "linear-gradient(to right, #1b1b1b, transparent)",
                zIndex: 1,
                pointerEvents: "none",
              }}
            />
            <Box
              sx={{
                position: "absolute",
                top: 0,
                right: 0,
                width: "100px",
                height: "100%",
                background: "linear-gradient(to left, #1b1b1b, transparent)",
                zIndex: 1,
                pointerEvents: "none",
              }}
            />

            {/* Animated Scroll Container */}
            <Stack
              direction="row"
              spacing={2}
              sx={{
                width: "max-content",
                animation: "scroll-left 50s linear infinite",
              }}
            >
              {[...Array(2)].flatMap(() => [
                <Card key="map" sx={{ width: 400, height: 400 }}>
                  <CardContent>
                    <Typography variant="overline" fontSize={14}>
                      Interactive Map
                    </Typography>
                    <Typography>
                      Clickable locations with linked lore, characters, and
                      shops.
                    </Typography>
                  </CardContent>
                </Card>,
                <Card key="fog" sx={{ width: 400, height: 400 }}>
                  <CardContent>
                    <Typography variant="overline" fontSize={14}>
                      Fog-of-War
                    </Typography>
                    <Typography>
                      Reveal regions as the party explores.
                    </Typography>
                  </CardContent>
                </Card>,
                <Card key="path" sx={{ width: 400, height: 400 }}>
                  <CardContent>
                    <Typography variant="overline" fontSize={14}>
                      Session Path Tracking
                    </Typography>
                    <Typography>
                      Visualize the party’s movement over time.
                    </Typography>
                  </CardContent>
                </Card>,
                <Card key="multi" sx={{ width: 400, height: 400 }}>
                  <CardContent>
                    <Typography variant="overline" fontSize={14}>
                      Multi-Campaign Support
                    </Typography>
                    <Typography>
                      Run multiple adventures in the same world with scoped
                      visibility.
                    </Typography>
                  </CardContent>
                </Card>,
                <Card key="journals" sx={{ width: 400, height: 400 }}>
                  <CardContent>
                    <Typography variant="overline" fontSize={14}>
                      Player Journals & Markers
                    </Typography>
                    <Typography>
                      Let players leave notes and track personal goals.
                    </Typography>
                  </CardContent>
                </Card>,
                <Card key="events" sx={{ width: 400, height: 400 }}>
                  <CardContent>
                    <Typography variant="overline" fontSize={14}>
                      World Events System
                    </Typography>
                    <Typography>
                      Global changes reflected across all campaigns.
                    </Typography>
                  </CardContent>
                </Card>,
              ])}
            </Stack>
          </Box>
        </section>
      </main>
    </div>
  );
};
