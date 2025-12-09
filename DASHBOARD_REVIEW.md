# Assignment Report: Evaluation of "Netflix in Numbers" Dashboard

**Course**: DSK808 Data Visualization
**Subject**: Compliance Review against Visualization Guidelines (Session 7 & 11)
**Date**: December 9, 2025

---

## 1. Introduction

The objective of this assignment was to critically evaluate the "Netflix in Numbers" interactive dashboard against the theoretical frameworks and practical guidelines established in the DSK808 course. Specifically, the review focuses on the application of Shneiderman's Mantra, color theory principles, and data-ink maximization strategies. The analysis reveals a dashboard that demonstrates a high degree of maturity in its design choices, particularly in its handling of accessibility and interaction patterns.

## 2. Interaction Design and Information Architecture

The dashboard's structural design serves as a textbook example of **Shneiderman's Mantra**: _"Overview first, zoom and filter, details on demand."_

The user journey begins with a global perspective via the `explore_by_country` Choropleth map, providing an immediate high-level overview of content distribution. This is not a static view; it invites interaction. By clicking on specific countries or adjusting the temporal sliders in `explore_by_time`, the user effectively "zooms and filters" the dataset. The "details on demand" are seamlessly integrated through hover interactions in the `ratings_comparison` scatter plot and the dynamic generation of country-specific histograms upon selection. This layered approach ensures that the user is never overwhelmed by the raw volume of data (8,000+ titles) but can access granular details when relevant.

## 3. Visual Encoding and Color Theory

A rigorous application of color theory is evident throughout the application, adhering to the guidelines from Session 7.

### 3.1. Sequential vs. Categorical Data

The dashboard avoids the common pitfall of using "rainbow" scales for quantitative data. Instead, it employs a custom **Sequential Red Scale** (`t["cont_scale"]`) for the choropleth map and heatmaps. This scale relies on luminance variation (dark to light/bright), making it perceptually uniform and intuitive: darker/brighter values clearly indicate "more" intensity.

### 3.2. Accessibility and Inclusion

A critical design intervention was made to address color blindness (specifically Deuteranopia). The initial design risked conflating Red and Green in categorical comparisons. To mitigate this, the palette was optimized by replacing the standard green with **Gold** (`#ffd700`). This ensures that the primary brand color (**Netflix Red**, `#e50914`) remains distinct against all other categorical variables, ensuring the dashboard is inclusive for all users.

### 3.3. Data-Ink Ratio

Following Tufte's principle of maximizing the data-ink ratio, the dashboard utilizes a dark theme (`#141414`) that recedes into the background. Gridlines are subtle (`#404040`), and borders are minimal. This "dark mode" approach is not merely aesthetic; it reduces eye strain and allows the bright data points to pop, focusing the user's attention strictly on the information being presented.

## 4. Critical Assessment of Chart Selection

The choice of visualization types is largely appropriate for the data types:

- **Geospatial Data**: Appropriately mapped using a Choropleth.
- **Hierarchical Data**: The `genre_analysis` component correctly utilizes a **Treemap** rather than a pie chart for the complex genre distribution, allowing for a clear comparison of relative areas.

### 4.1. Area for Improvement

However, a minor deviation from the strict "No Pie Charts" guideline is observed in the `genre_analysis` component. When a specific genre is selected, a Pie Chart is used to display the binary split between "Movies" and "TV Shows". While comparing two slices is generally cognitively manageable, the course guidelines explicitly discourage this form. A **Stacked Bar Chart** or a **Waffle Chart** would have been a more strictly compliant choice, eliminating the need for the user to compare angles and areas.

## 5. Conclusion

In conclusion, the "Netflix in Numbers" dashboard successfully translates theoretical visualization principles into a functional, user-centric application. It balances the strong aesthetic requirements of the Netflix brand with the rigorous demands of data clarity and accessibility. The proactive adjustment of the color palette to support color-blind users stands out as a highlight of the design process, demonstrating a commitment to inclusive design that goes beyond basic functionality.
