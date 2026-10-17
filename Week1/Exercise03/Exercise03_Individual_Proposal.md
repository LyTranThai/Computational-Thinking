# Exercise 03: Individual Proposal for Course Project

## Multimodal AI for Muscular Failure Prediction in Physical Training

- **Course:** Computational Thinking (CS252 - Class 25A01)
- **Student ID:** 25125048
- **Author:** Lý Trần Thái
- **Proposed Project Domain:** Biomechanics, Multimodal Machine Learning & Computational Ergonomics
- **Submission Date:** October 17, 2026

---

## 1. Executive Summary

In high-intensity resistance training, pushing sets close to momentary muscular failure is essential for maximizing neuromuscular adaptation and hypertrophic stimulus. However, accurately judging proximate failure—formulated in exercise science as **Reps in Reserve (RIR)** or **Rating of Perceived Exertion (RPE)**—is notoriously difficult for both novices and experienced lifters. Misjudging exhaustion frequently leads to catastrophic mechanical failure, uncontrolled drops under heavy free weights (e.g., bench press, squats, dips), and severe musculoskeletal injury.

This proposal introduces a **Multimodal AI System for Real-Time Muscular Failure Prediction**. By synthesizing high-frequency computer vision kinematics (barbell velocity loss, joint angular deceleration, and form breakdown) with wearable sensor telemetry (smartwatch inertial micro-tremors and surface electromyography signals), the system computes real-time physiological exertion curves, dynamically predicts remaining Reps in Reserve ($RIR \in [0, 3]$), and issues anticipatory safety alerts before catastrophic failure occurs.

---

## 2. Problem Statement & Motivation

### The Limitation of Unimodal Vision Systems
Existing commercial AI fitness applications (such as Apple Fitness+, Peloton Guide, or standard pose-estimation mobile apps) rely exclusively on single-camera computer vision to extract 2D/3D joint coordinates. While spatial keypoint models (e.g., MediaPipe Pose, YOLO-Pose) are effective for verifying geometric form (such as checking whether knees cave during squats or the lower back arches during deadlifts), **vision alone cannot measure internal muscular exertion, motor unit recruitment fatigue, or central nervous system exhaustion**.

In compound resistance exercises such as heavy barbell rows, dips, squats, and overhead presses:
1. **Geometric Invariance Prior to Failure:** A disciplined lifter often maintains flawless geometric posture right up to the penultimate repetition. The subsequent repetition suffers sudden mechanical failure mid-concentric phase, leaving standard vision models zero lead time to warn the user.
2. **Subjective RIR Inaccuracy:** Research in sports science demonstrates that lifters misjudge their actual RIR by an average of 1.5 to 2.5 repetitions, resulting in either sub-optimal training stimulus or dangerous overtraining.
3. **Absence of Intelligent Spotting:** Solo lifters without human spotters face real physical hazards when training to failure in home gyms or crowded fitness centers.

---

## 3. Independent Value & Differentiation from Group Project

In compliance with the assignment requirement for independent thinking:
- **Group Project Scope:** The collaborative group project focuses primarily on broad health informatics, basic workout session logging, and routine posture classification using standard web dashboards.
- **Individual Proposal Differentiation:**
  - **Distinct Problem Domain:** Real-time neuromuscular fatigue dynamics and biomechanical failure boundary prediction rather than static form evaluation.
  - **Novel Technical Approach:** Multimodal sensor fusion coupling high-speed optical kinematics ($60\text{ fps}$ video) with inertial measurement units (IMU high-frequency accelerometer/gyroscope signals) to capture sub-visual micro-tremors ($8 - 12\text{ Hz}$).
  - **Safety-Critical Feature Set:** Dynamic RIR regression and an anticipatory audio-haptic emergency warning trigger when the system detects imminent concentric stall, effectively functioning as an autonomous digital spotter.

---

## 4. Proposed Technical Architecture & Multimodal Pipeline

The proposed system operates through four modular layers:

```mermaid
flowchart TD
    subgraph Data Acquisition
        A["Smartphone Camera (60fps Video)"] --> B["Kinematic Extraction (MediaPipe / YOLO-Pose)"]
        C["Smartwatch / IMU Wearable"] --> D["Inertial Telemetry (Accel / Gyro 100Hz)"]
    end

    subgraph Feature Engineering
        B --> E["Kinematic Features: Velocity Loss (V_loss), Sticking Duration, Joint Deceleration"]
        D --> F["Physiological Features: Micro-tremor RMS, Spectral Energy (8-12 Hz)"]
    end

    subgraph Multimodal Fusion & Inference
        E --> G["Temporal Fusion Network (LSTM / Transformer)"]
        F --> G
        G --> H["Dynamic RIR Estimator: RIR in [0, 3]"]
        G --> I["Failure Risk Classifier: Safe / Warning / Critical"]
    end

    subgraph Safety Intervention
        I -->|Critical Failure Imminent| J["Real-time Audio Alert & Smartwatch Haptic Pulse"]
        H --> K["Post-Set Analytics & Velocity-Loss Dashboard"]
```

### Layer Details:
1. **Kinematic Feature Extraction:** Tracks barbell vertical trajectory, Mean Propulsive Velocity (MPV), and Concentric Peak Velocity. Velocity loss across repetitions within a set ($V_{\text{loss}}\% = \frac{V_1 - V_i}{V_1} \times 100$) serves as a primary mechanical indicator of fatigue.
2. **Physiological & Inertial Telemetry:** High-frequency (100 Hz) accelerometer and gyroscope data capture involuntary limb micro-tremors that emerge as motor units synchronize under high neuro-muscular strain.
3. **Multimodal Fusion Engine:** A lightweight temporal model aligns kinematic velocity curves with inertial tremor spectra to infer the instantaneous physiological reserve.
4. **Predictive Spotting & Interventions:** When predicted $RIR \le 0.5$ and instantaneous velocity drops below critical minimum threshold ($V_{\text{crit}} \approx 0.15\text{ m/s}$), the system delivers sub-second audio and haptic cues instructing the lifter to rack the bar safely.

---

## 5. Computational Thinking Methodology

This project directly demonstrates the four pillars of Computational Thinking:

| Computational Thinking Pillar | Application in Muscular Failure Prediction |
| :--- | :--- |
| **Decomposition** | Dividing the complex problem of physical exhaustion into isolated, measurable subsystems: barbell keypoint trajectory tracking, kinematic velocity derivation, temporal frequency analysis of micro-tremors, multimodal alignment, and rule-based safety alerts. |
| **Pattern Recognition** | Identifying empirical mathematical signatures preceding mechanical failure, specifically the exponential decay in Mean Propulsive Velocity (MPV) paired with power spectral density peaks in the $8 - 12\text{ Hz}$ tremor band. |
| **Abstraction** | Transforming noisy, high-dimensional raw pixel arrays and high-frequency sensor readings into simplified, normalized mathematical indices: relative velocity loss percentage ($V_{\text{loss}}\%$), sticking point duration ($\Delta t_{\text{stick}}$), and discrete Reps in Reserve estimates ($RIR \in \{0, 1, 2, 3\}$). |
| **Algorithm Design** | Designing a sliding-window temporal filtering algorithm that synchronizes asynchronous optical and inertial timestamps, calculates instantaneous deceleration, and triggers safety interventions with sub-200ms latency. |

---

## 6. Implementation Feasibility & Technology Stack

- **Computer Vision & Kinematics:** Python, OpenCV, MediaPipe Pose / YOLO-Pose lightweight ONNX models running on-device.
- **Signal Processing & Sensor Ingestion:** SciPy for Butterworth bandpass filtering ($8 - 12\text{ Hz}$ tremor isolation) and Fast Fourier Transform (FFT) feature extraction.
- **Model Inference:** Lightweight PyTorch / ONNX Runtime temporal regressor optimized for mobile execution ($< 25\text{ ms}$ per inference frame).
- **Client & Interface:** Responsive web/mobile dashboard built with Streamlit / React for real-time telemetry playback and post-workout exertion curves.

---

## 7. Conclusion

The Multimodal Muscular Failure Prediction system bridges the critical gap between visual movement aesthetics and internal muscular physiology. By grounding safety-critical training decisions in computational thinking, multimodal sensor fusion, and predictive machine learning, the project delivers a novel, practical, and intellectually rigorous contribution to sports engineering and injury prevention.
