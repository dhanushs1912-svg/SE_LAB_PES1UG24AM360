# Lab 1 — Requirements Engineering & UML Use-Case Modelling

**Dhanush S · PES1UG24AM360 · Section F**
PES University — Dept. of CSE
**Problem Statement #60 — Podcast Guest Scheduling & Outline Builder** *(Media, Events & Community)*

---

## Scenario

A media production organizer that lets podcast hosts share booking availability, collect guest
talking-point outlines, and generate timestamped run-of-show episode production notes.

| Actor | Kind | Role |
|---|---|---|
| Podcast Guest | Primary (human) | Books an interview slot, submits talking points and biography links |
| Show Host | Primary (human) | Publishes availability, reviews outlines, generates the run-of-show sheet |
| Calendar & Notification Service | Supporting (system) | Delivers calendar invites, confirmations and reminders |

The problem statement names only two stakeholders, but the lab handout requires at least three
actors. **Calendar & Notification Service** is modelled as a supporting actor because the supplied
FR-001 acceptance criteria already requires that a *"calendar invite [is] sent"* — implying an
external service boundary.

---

## Deliverables

| # | Deliverable | File |
|---|---|---|
| 1 | Requirements Table — 5 FRs + 2 NFRs | [Requirements_Table.docx](Requirements_Table.docx) |
| 2 | UML Use-Case Diagram | [UseCase_Diagram.pdf](UseCase_Diagram.pdf) |
| 3 | Use-Case Flow Specification | [UseCase_Flow_UC-01.docx](UseCase_Flow_UC-01.docx) |

---

## Use cases

| ID | Use case | Actor |
|---|---|---|
| UC-01 | Book Interview Slot | Podcast Guest |
| UC-02 | Submit Talking-Point Outline | Podcast Guest |
| UC-03 | Publish Availability | Show Host |
| UC-04 | Review & Approve Outline | Show Host |
| UC-05 | Generate Run-of-Show Sheet | Show Host |

**Relationships**

| Type | Relationship | Why |
|---|---|---|
| `«include»` | UC-01 → Validate Slot Availability | A booking **always** re-checks availability |
| `«include»` | UC-01 → Send Booking Notification | Every confirmed booking dispatches an invite |
| `«include»` | UC-05 → Export PDF Production Sheet | Generating the sheet always produces the PDF measured by NFR-001 |
| `«extend»` | Request Reschedule → UC-01 | **Optional** — only when the Guest asks to move a confirmed slot |
| `«extend»` | Attach Biography Links → UC-02 | **Optional** — a Guest may submit topics with no links |

`«include»` arrows point **base → included**; `«extend»` arrows point **extension → base**.

---

## Traceability

| Requirement | Realised by |
|---|---|
| FR-001 *(given)* | UC-01, UC-02 |
| FR-002 | UC-03 |
| FR-003 | UC-05 |
| FR-004 | UC-04 |
| FR-005 | Send Booking Notification *(«include» of UC-01)* |
| NFR-001 *(given)* | Export PDF Production Sheet *(«include» of UC-05)* |
| NFR-002 | Cross-cutting — every use case touching the episode board |
