# Facial Biometrics MVP / MVP de Biometría Facial

### 🇬🇧 English Summary
Demonstration MVP for a **facial recognition system** requested by client.  
Includes:
- Web Enrolment (Frontend demo)
- Central Server (FastAPI) → endpoints: `/api/enroll`, `/api/sync`, `/api/health`
- Local Agent (Flask) → offline verification (1:1 and 1:N)
- Bilingual docs (English / Spanish)

**⚠️ Note:** This is for demo purposes only — not production.  
Needs encryption (AES-256), JWT + MFA, and legal (RGPD/Chile) compliance before real use.

---

### 🇪🇸 Resumen en Español
MVP demostrativo de **reconocimiento facial** solicitado por el cliente.  
Incluye:
- Enrolamiento web (demo)
- Servidor central (FastAPI) → `/api/enroll`, `/api/sync`, `/api/health`
- Agente local (Flask) → verificación offline (1:1 y 1:N)
- Documentos bilingües (Inglés / Español)

**⚠️ Nota:** Solo para demostración.  
Antes de producción agregar cifrado AES-256, JWT + MFA y cumplimiento RGPD/Chile.

---

### 📄 Documentation files
All docs are in `/docs/`:
- `TEST_STEPS.md` → simple test checklist  
- `RISKS.md` → risks and recommendations

---

### 🧩 Recommended demo flow (for client meeting)
1. Enrol a new user (RUT + selfie)
2. Verify 1:1 with same person → show match result
3. Verify 1:N with unknown photo → show best match
4. Sync central → local agent
5. Show dashboard/health endpoint

---

### 📬 Contact
**Author:** Muzammal Hussain  
**Email:** your@email.com  
**GitHub:** [https://github.com/MuzammalHussain07](https://github.com/MuzammalHussain07)
