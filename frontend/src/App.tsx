import React, { useState } from 'react';
import { Container, Typography, Button, TextField, Card, CardContent, Grid, LinearProgress, Alert, Box } from '@mui/material';
import axios from 'axios';

interface ScoreData {
  credit_score: number;
  risk_level: string;
  probability_of_default: number;
  explanation: any;
  graph_data: any;
  message: string;
}

const App: React.FC = () => {
  const [features, setFeatures] = useState({
    upi_velocity: 0.85,
    gst_filings: 0.92,
    utility_consistency: 0.78
  });
  const [scoreData, setScoreData] = useState<ScoreData | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleScore = async () => {
    setLoading(true);
    setError('');
    try {
      const response = await axios.post('http://localhost:8000/api/score', {
        consent_token: 'mock-aa-consent-12345',
        features: features
      });
      setScoreData(response.data);
    } catch (err: any) {
      setError('Make sure backend is running on port 8000');
    }
    setLoading(false);
  };

  return (
    <Container maxWidth="lg" sx={{ mt: 4, mb: 6 }}>
      <Typography variant="h3" gutterBottom align="center" sx={{ fontWeight: 'bold' }}>
        AltCredit Nexus
      </Typography>
      <Typography variant="h6" align="center" color="text.secondary" gutterBottom>
        AI-Powered Privacy-First Credit Scoring for NTC & MSMEs
      </Typography>

      <Grid container spacing={4}>
        {/* Left: Input */}
        <Grid item xs={12} md={5}>
          <Card elevation={3}>
            <CardContent>
              <Typography variant="h6" gutterBottom>Alternative Data Input (Mock)</Typography>
              
              <TextField
                label="UPI Velocity (0-1)" fullWidth margin="normal" type="number" step="0.01"
                value={features.upi_velocity} onChange={(e) => setFeatures({...features, upi_velocity: parseFloat(e.target.value)})}
              />
              <TextField
                label="GST Filings Regularity (0-1)" fullWidth margin="normal" type="number" step="0.01"
                value={features.gst_filings} onChange={(e) => setFeatures({...features, gst_filings: parseFloat(e.target.value)})}
              />
              <TextField
                label="Utility Consistency (0-1)" fullWidth margin="normal" type="number" step="0.01"
                value={features.utility_consistency} onChange={(e) => setFeatures({...features, utility_consistency: parseFloat(e.target.value)})}
              />

              <Button 
                variant="contained" 
                color="primary" 
                fullWidth 
                size="large"
                onClick={handleScore}
                disabled={loading}
                sx={{ mt: 3, py: 1.5 }}
              >
                {loading ? 'AI Scoring in Progress...' : 'Generate Credit Score'}
              </Button>
            </CardContent>
          </Card>
        </Grid>

        {/* Right: Results */}
        <Grid item xs={12} md={7}>
          {error && <Alert severity="error" sx={{ mb: 2 }}>{error}</Alert>}

          {scoreData && (
            <Card elevation={3}>
              <CardContent>
                <Typography variant="h4" color="primary" gutterBottom>
                  Credit Score: <strong>{scoreData.credit_score}</strong>
                </Typography>

                <Box sx={{ my: 2 }}>
                  <LinearProgress 
                    variant="determinate" 
                    value={(scoreData.credit_score / 900) * 100} 
                    sx={{ height: 14, borderRadius: 2 }}
                    color={scoreData.risk_level === "Low" ? "success" : scoreData.risk_level === "Medium" ? "warning" : "error"}
                  />
                </Box>

                <Typography variant="h6">
                  Risk Level: <strong>{scoreData.risk_level}</strong>
                </Typography>
                <Typography>Probability of Default: <strong>{scoreData.probability_of_default}%</strong></Typography>

                <Typography variant="h6" sx={{ mt: 4 }}>Key Driving Factors</Typography>
                <ul style={{ paddingLeft: '20px' }}>
                  {scoreData.explanation.top_factors.map((item: any, i: number) => (
                    <li key={i}><strong>{item.factor}</strong>: {item.impact}</li>
                  ))}
                </ul>

                <Typography variant="body2" sx={{ mt: 3, fontStyle: 'italic' }}>
                  {scoreData.message}
                </Typography>
              </CardContent>
            </Card>
          )}
        </Grid>
      </Grid>
    </Container>
  );
};

export default App;
