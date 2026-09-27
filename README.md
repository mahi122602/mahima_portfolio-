# Mahima Thakar | Future Intelligence

A portfolio of data science, AI and machine learning by **Mahima Thakar**, a Master of Data Science student at Queensland University of Technology, Brisbane.

## Featured work

- **QUTwin:** ongoing athlete digital twin research and application development.
- **Brisbane 2032:** urban crisis intelligence prototype with risk modelling on simulated scenarios.
- **Traffic Anomaly Detection:** convolutional autoencoder pipeline for surveillance frames.
- **Australian Skills Shortage Analysis:** PostgreSQL and Power BI workforce analytics.

The portfolio includes experience, education, leadership, research interests, contact links and a downloadable résumé. Project details explain contribution and scope; concept artwork does not represent measured model performance.

## Interactive design

Teal `#008080`, slate blue `#6D8196` and cerise `#DD3162` form the visual identity. Features include cursor-responsive hero artwork, subtle card tilt, animated project filtering, scroll reveals, expandable research sections and project detail dialogs. Mobile controls work without hover. A motion toggle and system reduced-motion support are included.

The glass ribbon is generated artwork animated through CSS and pointer movement, not a real-time 3D model. All artwork and résumé bytes are bundled locally; the interface does not depend on external image hosting, API keys or a database.

## Deploy through GitHub

1. Extract the downloaded ZIP.
2. Create a GitHub repository, or open your existing portfolio repository.
3. Upload the **contents** of the extracted folder. `app.py`, `render.py`, `requirements.txt`, `assets/` and `.streamlit/` belong at the repository root. Upload the files, not the ZIP. Include the entire assets folder.
4. Commit to `main` (or your preferred deployment branch).
5. Open [Streamlit Community Cloud](https://share.streamlit.io), sign in with GitHub and choose **Create app** → deploy from GitHub.
6. Select your repository and branch. Set the main file path to **`app.py`**.
7. Under advanced settings, select **Python 3.12**. No secrets are needed.
8. Choose an available app URL, deploy, and ensure the app's sharing settings allow public access.

If your app is already deployed from this repository, commit the replacement files to its deployed branch. Keep the main file path correct. Reboot the app through its management menu if needed.

If `.streamlit` is hidden on your computer, enable hidden files before uploading, or create `.streamlit/config.toml` using GitHub's Add file button and copy its contents from this package. The app's own visual design also lives in `assets/portfolio.html`.

The hosted app does not require your laptop to remain on. Community Cloud apps can sleep after 12 hours without traffic, so free hosting is not guaranteed uninterrupted uptime; a visitor may need to wake the app.

Official references: [Deployment](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/deploy), [Dependencies](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/app-dependencies), [App management](https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-app).

## Run locally

Use Python 3.12. From the folder containing `app.py`:

```bash
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

Optional standalone browser preview:

```bash
python render.py
```

Then open the generated `preview.html`.

## Editing

| File | Purpose |
| --- | --- |
| `app.py` | Streamlit entry point and viewport wrapper |
| `render.py` | Embeds the local artwork and résumé |
| `assets/portfolio.html` | Editable content, styles and interactions |
| `assets/hero-ribbon.png` | Hero artwork |
| `assets/Mahima_Thakar_Resume.pdf` | Résumé downloaded by visitors |
| `requirements.txt` | Tested Streamlit dependency |
| `.streamlit/config.toml` | Streamlit theme configuration |

Replace the PDF with the same filename to update the résumé. Edit contact information, project copy and links in `assets/portfolio.html`. Keep placeholder tokens `__HERO_IMAGE__` and `__RESUME_BASE64__` intact. Internal links target the portfolio's embedded page; external project and social links open separately.

## Contact

[GitHub](https://github.com/mahi122602) · [LinkedIn](https://www.linkedin.com/in/mahi-thakar-2612mjt) · [Email](mailto:mahi.brissie25@gmail.com)
