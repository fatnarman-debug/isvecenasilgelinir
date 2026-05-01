# Design Decision Trees

> Logical flows for making consistent design choices.
> **Follow the logic, not your mood.**

---

## 1. Layout Selection Tree

**What is the primary user goal?**

- **Goal: Consume long-form content** (Articles, Documentation)
  └── **Single Column Centered Layout**
      ├── Max-width: 65-75ch
      └── Focus: Typography and whitespace

- **Goal: Data management & Analysis** (Dashboards, Tables)
  └── **Sidebar Navigation + Fluid Content Area**
      ├── Sidebar: Collapsible for focus
      └── Content Area: Grid-based (bento or dashboard)

- **Goal: Quick conversion / Marketing** (Landing Pages)
  └── **Z-Pattern or F-Pattern Hero Layout**
      ├── Visual → Headline → CTA
      └── Section-based scrolling

---

## 2. Interaction Design Tree

**The user clicked a button. What happens?**

- **Is the result immediate?** (<200ms)
  └── Show success state/feedback instantly.

- **Does it take time?** (>200ms)
  ├── **Is the duration predictable?**
  │   └── Show Progress Bar.
  └── **Is it unpredictable?**
      └── Show Skeleton Screen or Spinner.

- **Is the action critical?** (Delete, Unsubscribe)
  └── Trigger Confirmation Dialog (Modal).

---

## 3. Component Choice: Modal vs. Drawer vs. Inline

**How much context does the user need?**

- **Needs to see the current page while working?**
  └── **Inline Component** (Accordion, Expansion Tile).

- **Quick task that doesn't need full-page context?**
  └── **Drawer** (Slide-out from side).
      └── Best for filters, settings, or minor edits.

- **High-focus task or alert?**
  └── **Modal** (Center of screen).
      └── Best for confirmation, complex forms, or critical alerts.

---

## 4. Typography Scale Selection

**What is the application's density requirement?**

- **High Density** (Admin panels, IDEs, Trading tools)
  └── **Minor Second (1.067)** or **Major Second (1.125)**
      └── Focus on fitting more info without clutter.

- **Balanced UI** (SaaS apps, E-commerce, Portals)
  └── **Minor Third (1.2)** or **Major Third (1.25)**
      └── Focus on clear hierarchy and breathing room.

- **Visual/Editorial** (Blogs, Portfolios, Brand sites)
  └── **Perfect Fourth (1.333)** or **Golden Ratio (1.618)**
      └── Focus on dramatic headlines and aesthetic impact.

---

## 5. Color Mood Selection

**Who is the target audience?**

- **Professional/Enterprise**
  └── **Monochromatic / Analogous** (Cool tones)
      └── Primary: Slate/Navy. Accent: Steel Blue.

- **Startup/Modern**
  └── **High Contrast / Complementary**
      └── Primary: Dark Indigo. Accent: Electric Cyan.

- **Consumer/Lifestyle**
  └── **Warm / Earthy**
      └── Primary: Cream/Soft White. Accent: Terracotta.

---

## 6. Empty State Logic

**There is no data to show. What now?**

1. **Explain WHY**: "No results found for 'XYZ'."
2. **Value Prop**: "Connect your account to see your data."
3. **CTA**: "Create your first project" (Primary Button).
4. **Visual**: Simple, non-distracting illustration or icon.

---

## 7. Accessibility Validation Tree

1. **Does it work with keyboard?** (Tab index, Focus states)
2. **Is the contrast high enough?** (WCAG AA/AAA)
3. **Does it make sense to a screen reader?** (Aria labels, Roles)
4. **Does it work without color?** (Patterns, icons)

---

> **Implementation Note**: When presenting a design to the user, cite the path taken through these trees to justify your decisions.
