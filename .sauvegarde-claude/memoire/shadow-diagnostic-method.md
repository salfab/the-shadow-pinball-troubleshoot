---
name: shadow-diagnostic-method
description: "How the user wants the Bally The Shadow pinball repair diagnosis run (one measurement at a time, journal file, challenge hypotheses, annotated images of board parts)"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 67a0b140-c89f-4ca5-be8f-b924fa2c867f
  modified: 2026-10-25T16:53:44.069Z
---

For the Bally The Shadow (1994, WPC-S) Power Driver diagnosis, guide exactly one manipulation or measurement per message (where, how, how to interpret), then wait for the result. Off-power checks first, account for charged capacitors, and never suggest powering on before the pre-reconnection checklist is done. Treat the user's recollections as uncertain, never as confirmed diagnoses, and contradict them when evidence requires. Answer in French.

Whenever a message mentions a board component, connector, fuse or test point, also send an annotated image showing where it is (user asked on 2026-10-25). Use the user's own photo when it covers the spot; otherwise annotate the manual's layout (page 2-9) rotated 90° clockwise, which matches how the board is mounted in the backbox (J130 at the bottom, J101 on the right, fuses F101–F105 vertical with F101 left and F105 right). A pre-rotated copy is in `docs/manuel-the-shadow/2-9_PD_implantation_orientee-comme-montee.png`. Draw with PIL, save in `photos/`, send with SendUserFile.

Before asking for a series of measurements, say in one or two sentences what it protects against (the goal is never to reconnect a repaired Power Driver into a fault), and keep the series minimal: skip values already measured, try the most likely point first. The user questioned a 16-reading table ("À quoi ? Est-ce que ça me sert ?").

**Why:** the user asked for this explicitly; earlier unstructured measurements did not validate anything, and the Power Driver was already damaged several times. Finding parts from designators alone was hard for them.

**How to apply:** start each session by reading `journal-diagnostic-the-shadow.md` (project root) and the `docs/` and `photos/` folders next to it (manual pages, A-12697 schematic, user photos); update the journal after each significant step (measurement table, hypothesis status, next step). The manual's fuse table swaps F104 and F105 (the Power Driver schematic is right: F104 → J107-2 Red-Brown, F105 → J107-3 Red-Black) and its solenoid table has errors (Sol 08 is on Red-Black), so map coil supplies by measurement.
